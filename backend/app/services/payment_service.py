import random
import string
import uuid
from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.models.payment import Payment
from app.models.user import User


TIER_PRICES = {
    "pro": settings.PRICE_PRO,
    "max": settings.PRICE_MAX,
}


def _generate_ref() -> str:
    """Generate unique transaction ref like 360H-A3B7C2D8."""
    chars = string.ascii_uppercase + string.digits
    suffix = "".join(random.choices(chars, k=8))
    return f"360H-{suffix}"


def build_vietqr_url(amount: int, ref: str) -> str:
    """Construct VietQR image URL (img.vietqr.io — no API key needed)."""
    base = (
        f"https://img.vietqr.io/image/"
        f"{settings.BANK_BIN}-{settings.BANK_ACCOUNT_NUMBER}-compact2.png"
    )
    from urllib.parse import quote
    account_name_enc = quote(settings.BANK_ACCOUNT_NAME)
    return (
        f"{base}"
        f"?amount={amount}"
        f"&addInfo={ref}"
        f"&accountName={account_name_enc}"
    )


async def create_checkout(
    db: AsyncSession, user_id: uuid.UUID, tier: str
) -> Payment:
    if tier not in TIER_PRICES:
        raise ValueError(f"Invalid tier: {tier}")

    amount = TIER_PRICES[tier]

    # Generate unique ref (retry on collision)
    for _ in range(5):
        ref = _generate_ref()
        existing = await db.scalar(
            select(Payment).where(Payment.transaction_ref == ref)
        )
        if not existing:
            break

    payment = Payment(
        id=uuid.uuid4(),
        user_id=user_id,
        amount=amount,
        tier=tier,
        status="pending",
        transaction_ref=ref,
    )
    db.add(payment)
    await db.commit()
    await db.refresh(payment)
    return payment


async def get_payment_by_ref(db: AsyncSession, ref: str) -> Payment | None:
    return await db.scalar(
        select(Payment).where(Payment.transaction_ref == ref)
    )


async def submit_verification(
    db: AsyncSession, ref: str, bank_tx_id: str, user_id: uuid.UUID
) -> Payment | None:
    """User submits their bank transaction ID. Sets status to pending_verification."""
    payment = await get_payment_by_ref(db, ref)
    if not payment:
        return None
    if str(payment.user_id) != str(user_id):
        return None
    if payment.status != "pending":
        return payment  # already processed

    payment.bank_transaction_id = bank_tx_id
    payment.status = "pending_verification"
    payment.updated_at = datetime.now(timezone.utc)
    await db.commit()
    await db.refresh(payment)
    return payment


async def confirm_payment(
    db: AsyncSession, ref: str
) -> tuple[Payment | None, User | None]:
    """Admin/webhook confirms payment → upgrades user tier."""
    payment = await get_payment_by_ref(db, ref)
    if not payment or payment.status == "confirmed":
        return payment, None

    # Update payment
    payment.status = "confirmed"
    payment.confirmed_at = datetime.now(timezone.utc)
    payment.updated_at = datetime.now(timezone.utc)

    # Upgrade user tier
    user = await db.get(User, payment.user_id)
    if user:
        user.tier = payment.tier
        user.paid_at = payment.confirmed_at
        user.payment_ref = ref
        user.updated_at = datetime.now(timezone.utc)

    await db.commit()
    await db.refresh(payment)
    return payment, user
