from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Payment, Contract, Client
from schemas.payment import PaymentResponse

router = APIRouter()


@router.get("/", response_model=List[PaymentResponse])
async def get_my_payments(
    db: Session = Depends(get_db)
):
    """Get all payments (authentication removed)"""
    # Return all payments (no user filtering since JWT was removed)
    payments = db.query(Payment).all()
    return payments
