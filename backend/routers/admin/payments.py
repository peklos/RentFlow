from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Payment
from schemas.payment import PaymentResponse, PaymentUpdate

router = APIRouter()


@router.get("/", response_model=List[PaymentResponse])
async def get_all_payments(
    status: str = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(50, le=100),
    db: Session = Depends(get_db)
):
    """Get all payments (admin)"""
    query = db.query(Payment)

    if status:
        query = query.filter(Payment.payment_status == status)

    payments = query.offset(skip).limit(limit).all()
    return payments


@router.put("/{payment_id}", response_model=PaymentResponse)
async def update_payment(
    payment_id: int,
    payment_data: PaymentUpdate,
    db: Session = Depends(get_db)
):
    """Update payment (admin)"""
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Платеж не найден")

    update_data = payment_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(payment, field, value)

    db.commit()
    db.refresh(payment)

    return payment
