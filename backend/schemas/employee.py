from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime


class EmployeeLogin(BaseModel):
    login: str
    password: str


class EmployeeCreate(BaseModel):
    login: str
    password: str
    full_name: str
    position_id: int
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    hire_date: Optional[date] = None


class EmployeeUpdate(BaseModel):
    full_name: Optional[str] = None
    position_id: Optional[int] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None


class EmployeeResponse(BaseModel):
    id: int
    login: str
    full_name: str
    position_id: int
    phone: Optional[str] = None
    email: Optional[str] = None
    is_active: bool
    hire_date: Optional[date] = None
    created_at: datetime

    class Config:
        from_attributes = True
