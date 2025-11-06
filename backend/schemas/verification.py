from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class VerificationCreate(BaseModel):
    client_id: int
    verified_by: Optional[int] = None
    income_verified: bool = False
    credit_score: Optional[int] = None
    employment_verified: bool = False
    criminal_record_check: bool = False
    previous_rentals_check: bool = False
    result: str
    rejection_reason: Optional[str] = None
    notes: Optional[str] = None
    documents_checked: Optional[str] = None


class VerificationUpdate(BaseModel):
    income_verified: Optional[bool] = None
    credit_score: Optional[int] = None
    employment_verified: Optional[bool] = None
    criminal_record_check: Optional[bool] = None
    previous_rentals_check: Optional[bool] = None
    result: Optional[str] = None
    rejection_reason: Optional[str] = None
    notes: Optional[str] = None


class VerificationResponse(BaseModel):
    id: int
    client_id: int
    verified_by: Optional[int] = None
    verification_date: date
    income_verified: bool
    credit_score: Optional[int] = None
    employment_verified: bool
    criminal_record_check: bool
    previous_rentals_check: bool
    result: str
    rejection_reason: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
