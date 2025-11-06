from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Contract
from schemas.contract import ContractCreate, ContractUpdate, ContractResponse
from utils.security import require_role

router = APIRouter()


@router.post("/", response_model=ContractResponse, status_code=201)
async def create_contract(
    contract_data: ContractCreate,
    current_user: dict = Depends(require_role("employee")),
    db: Session = Depends(get_db)
):
    """Create a new contract (admin)"""
    new_contract = Contract(**contract_data.dict())
    db.add(new_contract)
    db.commit()
    db.refresh(new_contract)

    return new_contract


@router.get("/", response_model=List[ContractResponse])
async def get_all_contracts(
    status: str = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(50, le=100),
    current_user: dict = Depends(require_role("employee")),
    db: Session = Depends(get_db)
):
    """Get all contracts (admin)"""
    query = db.query(Contract)

    if status:
        query = query.filter(Contract.contract_status == status)

    contracts = query.offset(skip).limit(limit).all()
    return contracts


@router.put("/{contract_id}", response_model=ContractResponse)
async def update_contract(
    contract_id: int,
    contract_data: ContractUpdate,
    current_user: dict = Depends(require_role("employee")),
    db: Session = Depends(get_db)
):
    """Update contract (admin)"""
    contract = db.query(Contract).filter(Contract.id == contract_id).first()
    if not contract:
        raise HTTPException(status_code=404, detail="Contract not found")

    update_data = contract_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(contract, field, value)

    db.commit()
    db.refresh(contract)

    return contract
