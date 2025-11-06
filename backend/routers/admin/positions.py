from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Position
from schemas.position import PositionCreate, PositionResponse
from utils.security import require_role

router = APIRouter()


@router.post("/", response_model=PositionResponse, status_code=201)
async def create_position(
    position_data: PositionCreate,
    current_user: dict = Depends(require_role("employee")),
    db: Session = Depends(get_db)
):
    """Create a new position (admin)"""
    new_position = Position(**position_data.dict())
    db.add(new_position)
    db.commit()
    db.refresh(new_position)

    return new_position


@router.get("/", response_model=List[PositionResponse])
async def get_all_positions(
    current_user: dict = Depends(require_role("employee")),
    db: Session = Depends(get_db)
):
    """Get all positions (admin)"""
    positions = db.query(Position).all()
    return positions
