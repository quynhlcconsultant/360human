import uuid

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.profile import Profile
from app.schemas.profile import ProfileCreate, ProfileUpdate


async def get_profiles(db: AsyncSession, user_id: uuid.UUID) -> list[Profile]:
    result = await db.execute(
        select(Profile).where(Profile.user_id == user_id).order_by(Profile.created_at.desc())
    )
    return list(result.scalars().all())


async def get_profile(db: AsyncSession, profile_id: uuid.UUID, user_id: uuid.UUID) -> Profile:
    result = await db.execute(
        select(Profile).where(Profile.id == profile_id, Profile.user_id == user_id)
    )
    profile = result.scalar_one_or_none()
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hồ sơ không tồn tại")
    return profile


MAX_PROFILES_BY_TIER = {"free": 1, "pro": 3}


async def create_profile(
    db: AsyncSession, user_id: uuid.UUID, data: ProfileCreate, user_tier: str = "free"
) -> Profile:
    max_profiles = MAX_PROFILES_BY_TIER.get(user_tier, 1)
    existing = await get_profiles(db, user_id)
    if len(existing) >= max_profiles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Đã đạt giới hạn số lượng hồ sơ",
        )

    profile = Profile(user_id=user_id, **data.model_dump())
    db.add(profile)
    await db.commit()
    await db.refresh(profile)
    return profile


async def update_profile(
    db: AsyncSession, profile_id: uuid.UUID, user_id: uuid.UUID, data: ProfileUpdate
) -> Profile:
    profile = await get_profile(db, profile_id, user_id)
    for field, value in data.model_dump(exclude_none=True).items():
        setattr(profile, field, value)
    await db.commit()
    await db.refresh(profile)
    return profile


async def delete_profile(db: AsyncSession, profile_id: uuid.UUID, user_id: uuid.UUID) -> None:
    profile = await get_profile(db, profile_id, user_id)
    await db.delete(profile)
    await db.commit()
