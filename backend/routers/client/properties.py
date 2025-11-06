from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from decimal import Decimal

from db.database import get_db
from db.models import Property
from schemas.property import PropertyResponse

router = APIRouter()


@router.get("/", response_model=List[PropertyResponse])
async def get_properties(
    type: Optional[str] = None,
    min_price: Optional[Decimal] = None,
    max_price: Optional[Decimal] = None,
    min_area: Optional[Decimal] = None,
    max_area: Optional[Decimal] = None,
    rooms_count: Optional[int] = None,
    is_furnished: Optional[bool] = None,
    status: str = "available",
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db)
):
    """Get list of properties with filters"""
    query = db.query(Property)

    # Apply filters
    if type:
        query = query.filter(Property.type == type)
    if min_price is not None:
        query = query.filter(Property.monthly_rent >= min_price)
    if max_price is not None:
        query = query.filter(Property.monthly_rent <= max_price)
    if min_area is not None:
        query = query.filter(Property.area >= min_area)
    if max_area is not None:
        query = query.filter(Property.area <= max_area)
    if rooms_count is not None:
        query = query.filter(Property.rooms_count == rooms_count)
    if is_furnished is not None:
        query = query.filter(Property.is_furnished == is_furnished)
    if status:
        query = query.filter(Property.status == status)

    properties = query.offset(skip).limit(limit).all()
    return properties


@router.get("/{property_id}", response_model=PropertyResponse)
async def get_property(property_id: int, db: Session = Depends(get_db)):
    """Get property details by ID"""
    property = db.query(Property).filter(Property.id == property_id).first()
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")

    return property
