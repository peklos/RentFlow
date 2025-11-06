from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal


class ServiceCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    unit: Optional[str] = None
    is_active: bool = True


class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    unit: Optional[str] = None
    is_active: Optional[bool] = None


class ServiceResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: Decimal
    unit: Optional[str] = None
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
