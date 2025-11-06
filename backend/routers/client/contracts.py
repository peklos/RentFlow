from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Contract, Client
from schemas.contract import ContractResponse

router = APIRouter()


@router.get("/", response_model=List[ContractResponse])
async def get_my_contracts(
    db: Session = Depends(get_db)
):
    """Get all contracts (authentication removed)"""
    # Return all contracts (no user filtering since JWT was removed)
    contracts = db.query(Contract).all()
    return contracts


@router.get("/{contract_id}", response_model=ContractResponse)
async def get_contract(
    contract_id: int,
    db: Session = Depends(get_db)
):
    """Get specific contract details (authentication removed)"""
    contract = db.query(Contract).filter(Contract.id == contract_id).first()

    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")

    return contract
