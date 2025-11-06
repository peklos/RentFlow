from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Contract, Client
from schemas.contract import ContractResponse
from utils.security import get_current_user

router = APIRouter()


@router.get("/", response_model=List[ContractResponse])
async def get_my_contracts(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all contracts for current client"""
    if current_user["type"] != "client":
        raise HTTPException(status_code=403, detail="Not authorized")

    client = db.query(Client).filter(Client.user_id == current_user["id"]).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client profile not found")

    contracts = db.query(Contract).filter(Contract.client_id == client.id).all()
    return contracts


@router.get("/{contract_id}", response_model=ContractResponse)
async def get_contract(
    contract_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get specific contract details"""
    if current_user["type"] != "client":
        raise HTTPException(status_code=403, detail="Not authorized")

    client = db.query(Client).filter(Client.user_id == current_user["id"]).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client profile not found")

    contract = db.query(Contract).filter(
        Contract.id == contract_id,
        Contract.client_id == client.id
    ).first()

    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")

    return contract
