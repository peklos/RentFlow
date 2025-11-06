from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import AdditionalService
from schemas.service import ServiceResponse

router = APIRouter()


@router.get("/", response_model=List[ServiceResponse])
async def get_services(
    is_active: bool = True,
    skip: int = Query(0, ge=0),
    limit: int = Query(50, le=100),
    db: Session = Depends(get_db)
):
    """Get list of additional services"""
    query = db.query(AdditionalService)

    if is_active is not None:
        query = query.filter(AdditionalService.is_active == is_active)

    services = query.offset(skip).limit(limit).all()
    return services
