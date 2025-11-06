from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import AdditionalService
from schemas.service import ServiceCreate, ServiceUpdate, ServiceResponse

router = APIRouter()


@router.post("/", response_model=ServiceResponse, status_code=201)
async def create_service(
    service_data: ServiceCreate,
    db: Session = Depends(get_db)
):
    """Create a new additional service (admin)"""
    new_service = AdditionalService(**service_data.dict())
    db.add(new_service)
    db.commit()
    db.refresh(new_service)

    return new_service


@router.get("/", response_model=List[ServiceResponse])
async def get_all_services(
    db: Session = Depends(get_db)
):
    """Get all services (admin)"""
    services = db.query(AdditionalService).all()
    return services


@router.put("/{service_id}", response_model=ServiceResponse)
async def update_service(
    service_id: int,
    service_data: ServiceUpdate,
    db: Session = Depends(get_db)
):
    """Update service (admin)"""
    service = db.query(AdditionalService).filter(AdditionalService.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    update_data = service_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(service, field, value)

    db.commit()
    db.refresh(service)

    return service
