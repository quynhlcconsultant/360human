import json
import uuid
from datetime import datetime
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.user import User
from app.routers.auth import get_current_user
from app.schemas.profile import ProfileCreate, ProfileResponse, ProfileUpdate
from app.services.astrology_service import astrology_service
from app.services.profile_service import (
    create_profile,
    delete_profile,
    get_profile,
    get_profiles,
    update_profile,
)

router = APIRouter(prefix="/profiles", tags=["Profiles"])


@router.get("", response_model=list[ProfileResponse])
async def list_profiles(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await get_profiles(db, current_user.id)


@router.post("", response_model=ProfileResponse, status_code=status.HTTP_201_CREATED)
async def create(
    body: ProfileCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await create_profile(db, current_user.id, body, user_tier=current_user.tier)


@router.get("/{profile_id}", response_model=ProfileResponse)
async def get_one(
    profile_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await get_profile(db, profile_id, current_user.id)


@router.put("/{profile_id}", response_model=ProfileResponse)
async def update(
    profile_id: uuid.UUID,
    body: ProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await update_profile(db, profile_id, current_user.id, body)


@router.delete("/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    profile_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await delete_profile(db, profile_id, current_user.id)


@router.get("/{profile_id}/charts", response_model=dict[str, Any])
async def get_charts(
    profile_id: uuid.UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """
    Trả về raw chart data (L1) cho profile.
    Tính toán lần đầu rồi cache vào profile.chart_data.
    Backend LUÔN trả về cả 5 hệ thống (per ARCH-002).
    """
    profile = await get_profile(db, profile_id, current_user.id)

    if profile.chart_data:
        cached_systems = json.loads(profile.chart_data)
        has_errors = any(
            isinstance(v, dict) and v.get("error")
            for v in cached_systems.values()
        )
        if not has_errors:
            return {
                "profile_id": str(profile_id),
                "systems": cached_systems,
                "computed_at": profile.chart_computed_at.isoformat() if profile.chart_computed_at else None,
                "cached": True,
            }
        # Cache có lỗi → tính lại bên dưới

    # Chưa có cache → tính toán
    chart = await astrology_service.compute_all(
        birth_date=profile.birth_date,
        birth_time=profile.birth_time,
        birth_lat=profile.birth_lat,
        birth_lon=profile.birth_lon,
        birth_timezone=profile.birth_timezone,
        full_name=profile.full_name,
        gender=profile.gender,
    )
    profile.chart_data = json.dumps(chart, ensure_ascii=False)
    profile.chart_computed_at = datetime.utcnow()
    await db.commit()

    return {
        "profile_id": str(profile_id),
        "systems": chart,
        "computed_at": profile.chart_computed_at.isoformat(),
        "cached": False,
    }
