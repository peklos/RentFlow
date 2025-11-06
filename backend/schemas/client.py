from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime
from decimal import Decimal


class ClientCreate(BaseModel):
    full_name: str
    phone: str
    email: Optional[EmailStr] = None
    date_of_birth: Optional[date] = None


class ClientUpdate(BaseModel):
    full_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    passport_series: Optional[str] = None
    passport_number: Optional[str] = None
    passport_issued_by: Optional[str] = None
    passport_issue_date: Optional[date] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    alternative_phone: Optional[str] = None
    registration_address: Optional[str] = None
    actual_address: Optional[str] = None
    workplace: Optional[str] = None
    position: Optional[str] = None
    monthly_income: Optional[Decimal] = None


class ClientResponse(BaseModel):
    id: int
    full_name: str
    phone: str
    email: Optional[str] = None
    is_verified: bool
    client_type: str
    registration_date: date
    created_at: datetime

    class Config:
        from_attributes = True


class ClientProfile(BaseModel):
    id: int
    user_id: Optional[int] = None
    full_name: str
    date_of_birth: Optional[date] = None
    phone: str
    email: Optional[str] = None
    alternative_phone: Optional[str] = None
    registration_address: Optional[str] = None
    actual_address: Optional[str] = None
    workplace: Optional[str] = None
    position: Optional[str] = None
    monthly_income: Optional[Decimal] = None
    is_verified: bool
    client_type: str
    registration_date: date

    class Config:
        from_attributes = True
