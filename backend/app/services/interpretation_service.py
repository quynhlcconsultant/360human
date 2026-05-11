"""
L3: Claude AI Interpretation
Nhận enriched_context từ L2, gọi Claude API,
trả về Vietnamese prose theo tier word limit.
"""

import anthropic
from fastapi import HTTPException

from app.core.config import settings

TIER_WORD_LIMITS = {
    "free": 2000,
    "pro": 10000,
}

TIER_MODELS = {
    "free": "claude-haiku-4-5-20251001",
    "pro": "claude-sonnet-4-6",
}

SYSTEM_NAMES_VI = {
    "zi_wei": "Tử Vi Đẩu Số",
    "bazi": "Tứ Trụ (BaZi)",
    "human_design": "Human Design",
    "vedic": "Chiêm Tinh Vedic",
    "numerology": "Thần Số Học",
}

TOPIC_NAMES_VI = {
    "overview": "Tổng Quan Bản Mệnh",
    "love": "Tình Yêu & Hôn Nhân",
    "career": "Sự Nghiệp & Tài Chính",
    "health": "Sức Khỏe & Năng Lượng",
    "relationships": "Các Mối Quan Hệ",
    "purpose": "Sứ Mệnh & Mục Đích",
    "strengths": "Điểm Mạnh & Tài Năng",
    "challenges": "Thách Thức & Bài Học",
    "timing": "Vận Hạn & Thời Điểm",
    "spirituality": "Tâm Linh & Phát Triển",
}


def build_system_prompt(system: str, enriched_context: str, max_words: int) -> str:
    system_name = SYSTEM_NAMES_VI.get(system, system)
    return f"""Bạn là chuyên gia phân tích {system_name} hàng đầu, viết luận giải bằng tiếng Việt sâu sắc và cá nhân hóa.

DỮ LIỆU LÁ SỐ:
{enriched_context}

YÊU CẦU:
- Viết luận giải bằng tiếng Việt, văn phong tự nhiên, ấm áp và chuyên sâu
- Độ dài: khoảng {max_words} từ
- Cấu trúc: chia thành các đoạn rõ ràng với tiêu đề in đậm
- Tập trung vào ý nghĩa thực tiễn, không liệt kê thuật ngữ kỹ thuật
- Kết thúc bằng lời khuyên hành động cụ thể"""


def build_topic_prompt(topic: str, all_enriched: dict, max_words: int) -> str:
    topic_name = TOPIC_NAMES_VI.get(topic, topic)
    combined = "\n\n---\n\n".join(
        f"[{SYSTEM_NAMES_VI.get(sys, sys)}]\n{ctx}"
        for sys, ctx in all_enriched.items()
        if ctx
    )
    return f"""Bạn là chuyên gia tổng hợp 5 hệ thống chiêm tinh, phân tích chủ đề "{topic_name}" từ nhiều góc độ.

DỮ LIỆU TỪ 5 HỆ THỐNG:
{combined}

YÊU CẦU:
- Viết phân tích chủ đề "{topic_name}" bằng tiếng Việt
- Tổng hợp quan điểm từ các hệ thống có liên quan nhất
- Độ dài: khoảng {max_words} từ
- Ngôn ngữ đời thường, tập trung vào "Bạn nên làm gì" và "Cần lưu ý gì"
- Kết thúc bằng 3 hành động cụ thể"""


async def interpret_system(
    system: str,
    enriched_context: str,
    tier: str,
) -> str:
    """Gọi Claude để luận giải theo hệ thống."""
    max_words = TIER_WORD_LIMITS.get(tier, 2000)
    model = TIER_MODELS.get(tier, "claude-haiku-4-5-20251001")

    try:
        client = anthropic.AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)
        message = await client.messages.create(
            model=model,
            max_tokens=max_words * 2,  # tokens > words
            messages=[
                {
                    "role": "user",
                    "content": build_system_prompt(system, enriched_context, max_words),
                }
            ],
        )
        return message.content[0].text
    except anthropic.BadRequestError as e:
        raise HTTPException(status_code=503, detail=f"AI service unavailable: {str(e)}")
    except anthropic.APIStatusError as e:
        raise HTTPException(status_code=503, detail=f"AI service error: {e.status_code}")


async def interpret_topic(
    topic: str,
    all_enriched: dict,
    tier: str,
) -> str:
    """Gọi Claude để luận giải theo chủ đề, tổng hợp từ 5 hệ thống."""
    max_words = TIER_WORD_LIMITS.get(tier, 2000) // 5  # chia đều cho 10 topics
    model = TIER_MODELS.get(tier, "claude-haiku-4-5-20251001")

    try:
        client = anthropic.AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)
        message = await client.messages.create(
            model=model,
            max_tokens=max_words * 3,
            messages=[
                {
                    "role": "user",
                    "content": build_topic_prompt(topic, all_enriched, max_words),
                }
            ],
        )
        return message.content[0].text
    except anthropic.BadRequestError as e:
        raise HTTPException(status_code=503, detail=f"AI service unavailable: {str(e)}")
    except anthropic.APIStatusError as e:
        raise HTTPException(status_code=503, detail=f"AI service error: {e.status_code}")


def truncate_to_word_limit(text: str, max_words: int) -> str:
    """Cắt text về đúng giới hạn từ nếu cần."""
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]) + "…"
