from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Payment, Contract, Client
from schemas.payment import PaymentResponse
from utils.security import get_current_user

router = APIRouter()


@router.get("/", response_model=List[PaymentResponse])
async def get_my_payments(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all payments for current client"""
    if current_user["type"] != "client":
        raise HTTPException(status_code=403, detail="Not authorized")

    client = db.query(Client).filter(Client.user_id == current_user["id"]).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client profile not found")

    # Get all contracts for this client
    contracts = db.query(Contract).filter(Contract.client_id == client.id).all()
    contract_ids = [c.id for c in contracts]

    # Get payments for these contracts
    payments = db.query(Payment).filter(Payment.contract_id.in_(contract_ids)).all()
    return payments
