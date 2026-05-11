import uuid
from datetime import datetime

from pydantic import BaseModel, EmailStr, field_validator


# ─── Request schemas ──────────────────────────────────────


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def password_min_length(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("Mật khẩu phải có ít nhất 8 ký tự")
        return v


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


# ─── Response schemas ─────────────────────────────────────


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: uuid.UUID
    email: str
    tier: str
    is_active: bool
    paid_at: datetime | None
    created_at: datetime

    model_config = {"from_attributes": True}
