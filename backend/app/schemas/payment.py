from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CheckoutRequest(BaseModel):
    tier: str  # "pro" | "max"


class CheckoutResponse(BaseModel):
    payment_id: UUID
    transaction_ref: str
    amount: int
    tier: str
    vietqr_url: str
    bank_name: str
    account_number: str
    account_name: str
    status: str


class VerifyRequest(BaseModel):
    transaction_ref: str
    bank_transaction_id: str


class PaymentStatusResponse(BaseModel):
    transaction_ref: str
    status: str  # "pending" | "confirmed" | "cancelled"
    tier: str
    amount: int
    confirmed_at: Optional[datetime] = None


class WebhookConfirmRequest(BaseModel):
    transaction_ref: str
    webhook_secret: str
