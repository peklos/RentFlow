from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Company
from schemas.company import CompanyCreate, CompanyResponse

router = APIRouter()


@router.post("/", response_model=CompanyResponse, status_code=201)
async def create_company(
    company_data: CompanyCreate,
    db: Session = Depends(get_db)
):
    """Create a new company (admin)"""
    new_company = Company(**company_data.dict())
    db.add(new_company)
    db.commit()
    db.refresh(new_company)

    return new_company


@router.get("/", response_model=List[CompanyResponse])
async def get_all_companies(
    db: Session = Depends(get_db)
):
    """Get all companies (admin)"""
    companies = db.query(Company).all()
    return companies
