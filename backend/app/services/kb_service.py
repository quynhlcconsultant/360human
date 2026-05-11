"""
L2: Knowledge Base Loader + RAG
Đọc các file JSON/MD từ knowledge_base/, match với L1 raw data,
trả về enriched_context để đưa vào L3 Claude prompt.
"""

import json
import os
from functools import lru_cache
from pathlib import Path

KB_ROOT = Path(__file__).parent.parent.parent / "knowledge_base"


@lru_cache(maxsize=1)
def load_kb_index() -> dict:
    """Load _index.md và tất cả JSON files từ KB, cache in memory."""
    kb: dict = {}
    for system_dir in KB_ROOT.iterdir():
        if system_dir.is_dir() and not system_dir.name.startswith("_"):
            kb[system_dir.name] = {}
            for f in system_dir.iterdir():
                if f.suffix == ".json":
                    try:
                        with open(f, encoding="utf-8") as fp:
                            kb[system_dir.name][f.stem] = json.load(fp)
                    except Exception:
                        pass
                elif f.suffix == ".md":
                    try:
                        with open(f, encoding="utf-8") as fp:
                            kb[system_dir.name][f.stem] = fp.read()
                    except Exception:
                        pass
    return kb


def enrich_zi_wei(raw: dict, kb: dict) -> str:
    """Match Tử Vi raw data với KB rules. API v3 wraps data in raw['data']."""
    zi_wei_kb = kb.get("zi_wei", {})
    context_parts = []

    # API v3: data is under raw['data']
    data = raw.get("data", raw)

    palaces = data.get("palaces", [])
    if palaces:
        context_parts.append(f"Cung trong lá số: {json.dumps(palaces[:4], ensure_ascii=False)[:800]}")

    chart_data = data.get("chart_data", {})
    if chart_data:
        context_parts.append(f"Chart Data: {json.dumps(chart_data, ensure_ascii=False)[:600]}")

    four_trans = data.get("four_transformations", {})
    if four_trans:
        context_parts.append(f"Tứ Hóa: {json.dumps(four_trans, ensure_ascii=False)[:400]}")

    # Lookup chinh_tinh KB
    chinh_tinh = zi_wei_kb.get("chinh_tinh", "")
    if chinh_tinh and isinstance(chinh_tinh, str):
        context_parts.append(f"[KB Chính Tinh]\n{chinh_tinh[:2000]}")

    if not context_parts:
        context_parts.append(f"Zi Wei Dou Shu data: {json.dumps(data, ensure_ascii=False)[:1500]}")

    return "\n\n".join(context_parts)


def enrich_bazi(raw: dict, kb: dict) -> str:
    context_parts = []

    # API v3: data is under raw['data']
    data = raw.get("data", raw)

    four_pillars = data.get("four_pillars", {})
    if four_pillars:
        context_parts.append(f"Tứ Trụ: {json.dumps(four_pillars, ensure_ascii=False)[:600]}")

    day_master = data.get("day_master", {})
    if day_master:
        context_parts.append(f"Nhật Can: {json.dumps(day_master, ensure_ascii=False)[:300]}")

    elements = data.get("elements", {})
    if elements:
        context_parts.append(f"Ngũ Hành: {json.dumps(elements, ensure_ascii=False)[:300]}")

    personality = data.get("personality", {})
    if personality:
        context_parts.append(f"Tính Cách: {json.dumps(personality, ensure_ascii=False)[:400]}")

    luck_pillars = data.get("luck_pillars", [])
    if luck_pillars:
        items = luck_pillars[:3] if isinstance(luck_pillars, list) else luck_pillars
        context_parts.append(f"Đại Vận: {json.dumps(items, ensure_ascii=False)[:400]}")

    if not context_parts:
        context_parts.append(f"BaZi data: {json.dumps(data, ensure_ascii=False)[:1500]}")

    return "\n\n".join(context_parts)


def enrich_human_design(raw: dict, kb: dict) -> str:
    context_parts = []

    # API v3: data.bodygraph contains the main data
    data = raw.get("data", raw)
    bodygraph = data.get("bodygraph", data)

    hd_type = bodygraph.get("type", "")
    authority = bodygraph.get("authority", "")
    profile = bodygraph.get("profile", "")
    strategy = bodygraph.get("strategy", "")
    incarnation_cross = bodygraph.get("incarnation_cross", "")

    if hd_type:
        line = f"Type: {hd_type} | Authority: {authority} | Profile: {profile}"
        if strategy:
            line += f" | Strategy: {strategy}"
        if incarnation_cross:
            line += f" | Cross: {json.dumps(incarnation_cross, ensure_ascii=False)[:100]}"
        context_parts.append(line)

    for key in ("defined_centers", "centers"):
        val = bodygraph.get(key)
        if val:
            context_parts.append(f"Defined Centers: {json.dumps(val, ensure_ascii=False)[:400]}")
            break

    if not context_parts:
        context_parts.append(f"Human Design data: {json.dumps(data, ensure_ascii=False)[:1500]}")

    return "\n\n".join(context_parts)


def enrich_vedic(raw: dict, kb: dict) -> str:
    context_parts = []

    # API v3: data is under raw['data']
    # Keys: subject_name, planets, ascendant, moon_sign, sun_sign, nakshatra
    data = raw.get("data", raw)

    ascendant = data.get("ascendant", "")
    moon_sign = data.get("moon_sign", "")
    sun_sign = data.get("sun_sign", "")
    nakshatra = data.get("nakshatra", "")

    if ascendant or moon_sign:
        context_parts.append(
            f"Ascendant/Lagna: {ascendant} | Moon Sign (Rashi): {moon_sign} | Sun Sign: {sun_sign} | Nakshatra: {nakshatra}"
        )

    planets = data.get("planets", [])
    if planets:
        context_parts.append(f"Planets: {json.dumps(planets, ensure_ascii=False)[:800]}")

    if not context_parts:
        context_parts.append(f"Vedic data: {json.dumps(data, ensure_ascii=False)[:1500]}")

    return "\n\n".join(context_parts)


def enrich_numerology(raw: dict, kb: dict) -> str:
    """
    Đọc numerology data từ astrology-api.io response.
    API v3: data under raw['data'], keys: core_numbers, cycles, summary, strengths, life_lessons
    """
    numerology_kb = kb.get("numerology", {})
    context_parts = []

    # API v3: data is under raw['data']
    data = raw.get("data", raw)
    core_numbers = data.get("core_numbers", {})

    if core_numbers:
        life_path = core_numbers.get("life_path", {})
        expression = core_numbers.get("expression", {})
        soul_urge = core_numbers.get("soul_urge", {})
        personality = core_numbers.get("personality", {})

        parts = []
        if life_path:
            num = life_path.get("number", life_path) if isinstance(life_path, dict) else life_path
            parts.append(f"Life Path: {num}")
        if expression:
            num = expression.get("number", expression) if isinstance(expression, dict) else expression
            parts.append(f"Expression: {num}")
        if soul_urge:
            num = soul_urge.get("number", soul_urge) if isinstance(soul_urge, dict) else soul_urge
            parts.append(f"Soul Urge: {num}")
        if personality:
            num = personality.get("number", personality) if isinstance(personality, dict) else personality
            parts.append(f"Personality: {num}")
        if parts:
            context_parts.append(" | ".join(parts))

    summary = data.get("summary", "")
    if summary:
        context_parts.append(f"Summary: {summary[:500]}")

    strengths = data.get("strengths", [])
    if strengths:
        context_parts.append(f"Strengths: {json.dumps(strengths[:5], ensure_ascii=False)[:300]}")

    # Lookup KB life_path
    life_path_val = core_numbers.get("life_path", {})
    if isinstance(life_path_val, dict):
        life_path_val = life_path_val.get("number", "")
    life_path_kb = numerology_kb.get("life_path", "")
    if life_path_val and life_path_kb and isinstance(life_path_kb, str):
        context_parts.append(f"[KB Life Path {life_path_val}]\n{life_path_kb[:1000]}")

    if not context_parts:
        context_parts.append(f"Numerology data: {json.dumps(data, ensure_ascii=False)[:1000]}")

    return "\n\n".join(context_parts)


def build_enriched_context(chart_data: dict, system: str | None = None) -> dict:
    """
    chart_data: output từ AstrologyService.compute_all()
    system: None = tất cả 5 hệ thống, hoặc "zi_wei" | "bazi" | ...
    Returns: dict {system_name: enriched_context_string}
    """
    kb = load_kb_index()
    enrichers = {
        "zi_wei": enrich_zi_wei,
        "bazi": enrich_bazi,
        "human_design": enrich_human_design,
        "vedic": enrich_vedic,
        "numerology": enrich_numerology,
    }

    systems = [system] if system else list(enrichers.keys())
    result = {}
    for sys_name in systems:
        raw = chart_data.get(sys_name, {})
        if raw and not raw.get("error"):
            fn = enrichers.get(sys_name)
            if fn:
                result[sys_name] = fn(raw, kb)
    return result
