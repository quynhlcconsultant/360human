import uuid
from datetime import date, datetime
from typing import Any

from pydantic import BaseModel, field_validator


class ProfileCreate(BaseModel):
    full_name: str
    birth_date: date
    birth_time: str | None = None       # "HH:MM"
    birth_city: str | None = None
    birth_lat: str | None = None
    birth_lon: str | None = None
    birth_timezone: str | None = "Asia/Ho_Chi_Minh"
    gender: str | None = None

    @field_validator("birth_time")
    @classmethod
    def validate_time_format(cls, v: str | None) -> str | None:
        if v is None:
            return v
        parts = v.split(":")
        if len(parts) != 2 or not all(p.isdigit() for p in parts):
            raise ValueError("birth_time phải có định dạng HH:MM")
        return v


class ProfileUpdate(BaseModel):
    full_name: str | None = None
    birth_time: str | None = None
    birth_city: str | None = None
    birth_lat: str | None = None
    birth_lon: str | None = None
    birth_timezone: str | None = None
    gender: str | None = None


class ProfileResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    full_name: str
    birth_date: date
    birth_time: str | None
    birth_city: str | None
    birth_lat: str | None
    birth_lon: str | None
    birth_timezone: str | None
    gender: str | None
    chart_computed_at: datetime | None
    created_at: datetime

    model_config = {"from_attributes": True}


class ChartResponse(BaseModel):
    profile_id: uuid.UUID
    systems: dict[str, Any]             # raw chart data per system
    computed_at: datetime | None
