from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import Client, UserClient
from schemas.client import ClientProfile, ClientUpdate
from utils.security import get_current_user

router = APIRouter()


@router.get("/me", response_model=ClientProfile)
async def get_my_profile(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get current user's profile"""
    if current_user["type"] != "client":
        raise HTTPException(status_code=403, detail="Not authorized")

    client = db.query(Client).filter(Client.user_id == current_user["id"]).first()
    if not client:
        raise HTTPException(status_code=404, detail="Profile not found")

    return client


@router.put("/me", response_model=ClientProfile)
async def update_my_profile(
    profile_data: ClientUpdate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update current user's profile"""
    if current_user["type"] != "client":
        raise HTTPException(status_code=403, detail="Not authorized")

    client = db.query(Client).filter(Client.user_id == current_user["id"]).first()
    if not client:
        raise HTTPException(status_code=404, detail="Profile not found")

    # Update fields
    update_data = profile_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(client, field, value)

    db.commit()
    db.refresh(client)

    return client
