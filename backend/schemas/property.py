from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal


class PropertyCreate(BaseModel):
    type: str = Field(..., description="commercial or residential")
    subtype: Optional[str] = None
    address: str
    area: Decimal
    rooms_count: Optional[int] = None
    floor: Optional[int] = None
    total_floors: Optional[int] = None
    renovation_type: Optional[str] = None
    is_furnished: bool = False
    monthly_rent: Decimal
    utilities_included: bool = False
    deposit_amount: Optional[Decimal] = None
    description: Optional[str] = None
    amenities: Optional[str] = None
    photos: Optional[str] = None
    video_url: Optional[str] = None
    status: str = "available"


class PropertyUpdate(BaseModel):
    type: Optional[str] = None
    subtype: Optional[str] = None
    address: Optional[str] = None
    area: Optional[Decimal] = None
    rooms_count: Optional[int] = None
    floor: Optional[int] = None
    total_floors: Optional[int] = None
    renovation_type: Optional[str] = None
    is_furnished: Optional[bool] = None
    monthly_rent: Optional[Decimal] = None
    utilities_included: Optional[bool] = None
    deposit_amount: Optional[Decimal] = None
    description: Optional[str] = None
    amenities: Optional[str] = None
    photos: Optional[str] = None
    video_url: Optional[str] = None
    status: Optional[str] = None


class PropertyResponse(BaseModel):
    id: int
    type: str
    subtype: Optional[str] = None
    address: str
    area: Decimal
    rooms_count: Optional[int] = None
    floor: Optional[int] = None
    total_floors: Optional[int] = None
    renovation_type: Optional[str] = None
    is_furnished: bool
    monthly_rent: Decimal
    utilities_included: bool
    deposit_amount: Optional[Decimal] = None
    description: Optional[str] = None
    amenities: Optional[str] = None
    photos: Optional[str] = None
    video_url: Optional[str] = None
    status: str
    published_at: Optional[datetime] = None
    created_at: datetime

    class Config:
        from_attributes = True


class PropertyFilter(BaseModel):
    type: Optional[str] = None
    min_price: Optional[Decimal] = None
    max_price: Optional[Decimal] = None
    min_area: Optional[Decimal] = None
    max_area: Optional[Decimal] = None
    rooms_count: Optional[int] = None
    is_furnished: Optional[bool] = None
    status: Optional[str] = "available"
