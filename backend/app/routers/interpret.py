"""
Interpret endpoints — L1 → L2 → L3 pipeline với Redis cache
GET /interpret/system/{framework}/{profile_id}
GET /interpret/topic/{domain}/{profile_id}
"""

import json
import uuid
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status  # status dùng ở DELETE endpoint
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.redis import get_redis
from app.models.user import User
from app.routers.auth import get_current_user
from app.services.astrology_service import astrology_service
from app.services.interpretation_service import (
    TOPIC_NAMES_VI,
    interpret_system,
    interpret_topic,
    truncate_to_word_limit,
)
from app.services.kb_service import build_enriched_context
from app.services.profile_service import get_profile

router = APIRouter(prefix="/interpret", tags=["Interpretation"])

CACHE_TTL = 60 * 60 * 24 * 30  # 30 ngày

VALID_SYSTEMS = ["zi_wei", "bazi", "human_design", "vedic", "numerology"]
VALID_TOPICS = list(TOPIC_NAMES_VI.keys())

# Tier word limits — backend chỉ enforce max_words (per ARCH-002)
# Frontend tier-gate.tsx xử lý blur/truncate UI
SYSTEM_WORD_LIMITS = {"free": 500, "pro": 2000}   # 500w preview cho free, 2000w full cho pro
TOPIC_WORD_LIMITS  = {"free": 1000, "pro": 1000}   # 2000w tổng / 2 topics free; 10000w / 10 topics pro


def _has_errors(chart: dict) -> bool:
    """Kiểm tra nếu cached chart data có lỗi từ API calls trước."""
    return any(
        isinstance(v, dict) and v.get("error")
        for v in chart.values()
    )


async def _get_or_compute_chart(profile, db) -> dict:
    """Lấy chart data từ DB cache hoặc tính lại."""
    if profile.chart_data:
        cached = json.loads(profile.chart_data)
        if not _has_errors(cached):
            return cached
        # Cache có lỗi → tính lại

    chart = await astrology_service.compute_all(
        birth_date=profile.birth_date,
        birth_time=profile.birth_time,
        birth_lat=profile.birth_lat,
        birth_lon=profile.birth_lon,
        birth_timezone=profile.birth_timezone,
        full_name=profile.full_name,
        gender=profile.gender,
    )
    # Lưu lại vào profile
    profile.chart_data = json.dumps(chart, ensure_ascii=False)
    profile.chart_computed_at = datetime.utcnow()
    await db.commit()
    return chart


@router.get("/system/{framework}/{profile_id}")
async def interpret_system_endpoint(
    framework: str,
    profile_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    if framework not in VALID_SYSTEMS:
        raise HTTPException(status_code=400, detail=f"Hệ thống không hợp lệ: {framework}")

    profile = await get_profile(db, profile_id, current_user.id)

    # Check Redis cache
    redis = await get_redis()
    cache_key = f"system:{framework}:{profile_id}:{current_user.tier}"
    if redis:
        cached = await redis.get(cache_key)
        if cached:
            return json.loads(cached)

    # Compute
    chart_data = await _get_or_compute_chart(profile, db)
    enriched = build_enriched_context(chart_data, system=framework)
    context = enriched.get(framework, "")

    if not context:
        raise HTTPException(status_code=422, detail="Không thể tính toán dữ liệu cho hệ thống này")

    text = await interpret_system(framework, context, current_user.tier)
    # Backend chỉ enforce word limit — frontend xử lý blur/lock UI (ARCH-002)
    max_words = SYSTEM_WORD_LIMITS.get(current_user.tier, 500)
    text = truncate_to_word_limit(text, max_words)

    result = {
        "profile_id": str(profile_id),
        "framework": framework,
        "tier": current_user.tier,
        "interpretation": text,
        "word_count": len(text.split()),
    }

    if redis:
        await redis.setex(cache_key, CACHE_TTL, json.dumps(result, ensure_ascii=False))

    return result


@router.get("/topic/{domain}/{profile_id}")
async def interpret_topic_endpoint(
    domain: str,
    profile_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    if domain not in VALID_TOPICS:
        raise HTTPException(status_code=400, detail=f"Chủ đề không hợp lệ: {domain}")

    profile = await get_profile(db, profile_id, current_user.id)

    # Check Redis cache
    redis = await get_redis()
    cache_key = f"topic:{domain}:{profile_id}:{current_user.tier}"
    if redis:
        cached = await redis.get(cache_key)
        if cached:
            return json.loads(cached)

    chart_data = await _get_or_compute_chart(profile, db)
    all_enriched = build_enriched_context(chart_data)

    text = await interpret_topic(domain, all_enriched, current_user.tier)
    # Backend chỉ enforce word limit — frontend xử lý blur/lock UI (ARCH-002)
    max_words = TOPIC_WORD_LIMITS.get(current_user.tier, 1000)
    text = truncate_to_word_limit(text, max_words)

    result = {
        "profile_id": str(profile_id),
        "domain": domain,
        "tier": current_user.tier,
        "interpretation": text,
        "word_count": len(text.split()),
    }

    if redis:
        await redis.setex(cache_key, CACHE_TTL, json.dumps(result, ensure_ascii=False))

    return result


@router.delete("/cache/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def clear_cache(
    profile_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
):
    """Xóa cache khi profile được cập nhật."""
    redis = await get_redis()
    if redis:
        keys = await redis.keys(f"*:{profile_id}:*")
        if keys:
            await redis.delete(*keys)
