from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db
from app.models.user import User
from app.routers.auth import get_current_user
from app.schemas.payment import (
    CheckoutRequest,
    CheckoutResponse,
    PaymentStatusResponse,
    VerifyRequest,
    WebhookConfirmRequest,
)
from app.services import payment_service

router = APIRouter(prefix="/payments", tags=["Payments"])


@router.post("/checkout", response_model=CheckoutResponse)
async def checkout(
    body: CheckoutRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Create a pending payment and return a VietQR URL."""
    if current_user.tier == body.tier:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Bạn đã ở gói {body.tier.upper()} rồi.",
        )

    payment = await payment_service.create_checkout(db, current_user.id, body.tier)
    vietqr_url = payment_service.build_vietqr_url(payment.amount, payment.transaction_ref)

    return CheckoutResponse(
        payment_id=payment.id,
        transaction_ref=payment.transaction_ref,
        amount=payment.amount,
        tier=payment.tier,
        vietqr_url=vietqr_url,
        bank_name="Vietcombank",
        account_number=settings.BANK_ACCOUNT_NUMBER,
        account_name=settings.BANK_ACCOUNT_NAME,
        status=payment.status,
    )


@router.post("/verify")
async def verify_payment(
    body: VerifyRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """User submits bank transaction ID after transferring money."""
    payment = await payment_service.submit_verification(
        db, body.transaction_ref, body.bank_transaction_id, current_user.id
    )
    if not payment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Không tìm thấy giao dịch.",
        )
    return {"status": payment.status, "message": "Đã ghi nhận. Chúng tôi sẽ xác nhận trong vài phút."}


@router.get("/status/{ref}", response_model=PaymentStatusResponse)
async def payment_status(
    ref: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Poll payment status (frontend polls every 5s after user submits verification)."""
    payment = await payment_service.get_payment_by_ref(db, ref)
    if not payment or str(payment.user_id) != str(current_user.id):
        raise HTTPException(status_code=404, detail="Không tìm thấy giao dịch.")

    return PaymentStatusResponse(
        transaction_ref=payment.transaction_ref,
        status=payment.status,
        tier=payment.tier,
        amount=payment.amount,
        confirmed_at=payment.confirmed_at,
    )


@router.post("/webhook/confirm")
async def webhook_confirm(
    body: WebhookConfirmRequest,
    db: AsyncSession = Depends(get_db),
):
    """Admin/bank webhook confirms payment. Protected by shared WEBHOOK_SECRET."""
    if body.webhook_secret != settings.WEBHOOK_SECRET:
        raise HTTPException(status_code=403, detail="Invalid webhook secret.")

    payment, user = await payment_service.confirm_payment(db, body.transaction_ref)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found.")

    return {
        "status": "confirmed",
        "transaction_ref": payment.transaction_ref,
        "user_tier": user.tier if user else None,
    }
