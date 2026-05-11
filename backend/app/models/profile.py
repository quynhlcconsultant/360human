import uuid
from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )

    # Birth data
    full_name: Mapped[str] = mapped_column(String(200), nullable=False)
    birth_date: Mapped[date] = mapped_column(Date, nullable=False)
    birth_time: Mapped[str | None] = mapped_column(String(10), nullable=True)   # "HH:MM"
    birth_city: Mapped[str | None] = mapped_column(String(200), nullable=True)
    birth_lat: Mapped[str | None] = mapped_column(String(20), nullable=True)
    birth_lon: Mapped[str | None] = mapped_column(String(20), nullable=True)
    birth_timezone: Mapped[str | None] = mapped_column(String(60), nullable=True)  # "Asia/Ho_Chi_Minh"
    gender: Mapped[str | None] = mapped_column(String(10), nullable=True)       # "male" | "female"

    # Chart cache (raw JSON from astrology-api.io)
    chart_data: Mapped[str | None] = mapped_column(Text, nullable=True)         # JSON string
    chart_computed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
    )

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="profiles")  # type: ignore

    def __repr__(self) -> str:
        return f"<Profile id={self.id} name={self.full_name}>"
