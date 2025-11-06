from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Property
from schemas.property import PropertyCreate, PropertyUpdate, PropertyResponse
from utils.security import require_role

router = APIRouter()


@router.post("/", response_model=PropertyResponse, status_code=201)
async def create_property(
    property_data: PropertyCreate,
    current_user: dict = Depends(require_role("employee")),
    db: Session = Depends(get_db)
):
    """Create a new property"""
    new_property = Property(**property_data.dict())
    db.add(new_property)
    db.commit()
    db.refresh(new_property)

    return new_property


@router.get("/", response_model=List[PropertyResponse])
async def get_all_properties(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, le=100),
    current_user: dict = Depends(require_role("employee")),
    db: Session = Depends(get_db)
):
    """Get all properties (admin)"""
    properties = db.query(Property).offset(skip).limit(limit).all()
    return properties


@router.put("/{property_id}", response_model=PropertyResponse)
async def update_property(
    property_id: int,
    property_data: PropertyUpdate,
    current_user: dict = Depends(require_role("employee")),
    db: Session = Depends(get_db)
):
    """Update property"""
    property = db.query(Property).filter(Property.id == property_id).first()
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")

    update_data = property_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(property, field, value)

    db.commit()
    db.refresh(property)

    return property


@router.delete("/{property_id}")
async def delete_property(
    property_id: int,
    current_user: dict = Depends(require_role("employee")),
    db: Session = Depends(get_db)
):
    """Delete property"""
    property = db.query(Property).filter(Property.id == property_id).first()
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")

    db.delete(property)
    db.commit()

    return {"message": "Property deleted successfully"}
