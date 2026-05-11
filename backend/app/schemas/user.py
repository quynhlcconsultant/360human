from pydantic import BaseModel, EmailStr


class UserUpdate(BaseModel):
    """Cho phép user tự update thông tin cơ bản."""
    email: EmailStr | None = None


class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str

    class Config:
        json_schema_extra = {
            "example": {
                "current_password": "oldpassword123",
                "new_password": "newpassword456",
            }
        }
