from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import TenantVerification
from schemas.verification import VerificationCreate, VerificationResponse
from utils.security import require_role

router = APIRouter()


@router.post("/", response_model=VerificationResponse, status_code=201)
async def create_verification(
    verification_data: VerificationCreate,
    current_user: dict = Depends(require_role("employee")),
    db: Session = Depends(get_db)
):
    """Create tenant verification (admin)"""
    new_verification = TenantVerification(**verification_data.dict())
    db.add(new_verification)
    db.commit()
    db.refresh(new_verification)

    return new_verification


@router.get("/", response_model=List[VerificationResponse])
async def get_all_verifications(
    current_user: dict = Depends(require_role("employee")),
    db: Session = Depends(get_db)
):
    """Get all verifications (admin)"""
    verifications = db.query(TenantVerification).all()
    return verifications
