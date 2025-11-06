from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class ApplicationCreate(BaseModel):
    property_id: int
    preferred_move_in_date: Optional[date] = None
    lease_duration_months: Optional[int] = None
    notes: Optional[str] = None


class ApplicationUpdate(BaseModel):
    status: Optional[str] = None
    preferred_move_in_date: Optional[date] = None
    lease_duration_months: Optional[int] = None
    notes: Optional[str] = None
    rejection_reason: Optional[str] = None


class ApplicationResponse(BaseModel):
    id: int
    client_id: int
    property_id: int
    application_date: date
    status: str
    preferred_move_in_date: Optional[date] = None
    lease_duration_months: Optional[int] = None
    notes: Optional[str] = None
    rejection_reason: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
