from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime


class ReviewCreate(BaseModel):
    property_id: Optional[int] = None
    rating: int = Field(..., ge=1, le=5)
    text: Optional[str] = None


class ReviewUpdate(BaseModel):
    is_approved: Optional[bool] = None


class ReviewResponse(BaseModel):
    id: int
    client_id: int
    property_id: Optional[int] = None
    rating: int
    text: Optional[str] = None
    review_date: date
    is_approved: bool
    created_at: datetime

    class Config:
        from_attributes = True
