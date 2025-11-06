from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CompanyCreate(BaseModel):
    name: str
    inn: Optional[str] = None
    legal_address: Optional[str] = None


class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    inn: Optional[str] = None
    legal_address: Optional[str] = None


class CompanyResponse(BaseModel):
    id: int
    name: str
    inn: Optional[str] = None
    legal_address: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
