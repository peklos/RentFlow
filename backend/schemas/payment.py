from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from decimal import Decimal


class PaymentCreate(BaseModel):
    contract_id: int
    payment_date: date
    amount: Decimal
    payment_type: str = "rent"
    payment_method: Optional[str] = None
    period_month: Optional[int] = None
    period_year: Optional[int] = None


class PaymentUpdate(BaseModel):
    payment_status: Optional[str] = None
    transaction_id: Optional[str] = None
    is_late: Optional[bool] = None
    late_days: Optional[int] = None
    penalty_amount: Optional[Decimal] = None
    notes: Optional[str] = None


class PaymentResponse(BaseModel):
    id: int
    contract_id: int
    payment_date: date
    amount: Decimal
    payment_type: str
    payment_method: Optional[str] = None
    payment_status: str
    transaction_id: Optional[str] = None
    period_month: Optional[int] = None
    period_year: Optional[int] = None
    is_late: bool
    late_days: int
    penalty_amount: Decimal
    created_at: datetime

    class Config:
        from_attributes = True
