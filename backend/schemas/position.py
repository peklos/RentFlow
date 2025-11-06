from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PositionCreate(BaseModel):
    name: str
    description: Optional[str] = None
    access_level: int = 1


class PositionUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    access_level: Optional[int] = None


class PositionResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    access_level: int
    created_at: datetime

    class Config:
        from_attributes = True
