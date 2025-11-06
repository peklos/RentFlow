from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import Client
from schemas.client import ClientProfile, ClientUpdate

router = APIRouter()


@router.get("/{client_id}", response_model=ClientProfile)
async def get_profile(client_id: int, db: Session = Depends(get_db)):
    """Get client profile by ID"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Профиль не найден")
    return client


@router.get("/", response_model=list[ClientProfile])
async def get_all_profiles(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, le=100),
    db: Session = Depends(get_db)
):
    """Get all client profiles"""
    clients = db.query(Client).offset(skip).limit(limit).all()
    return clients


@router.put("/{client_id}", response_model=ClientProfile)
async def update_profile(
    client_id: int,
    profile_data: ClientUpdate,
    db: Session = Depends(get_db)
):
    """Update client profile"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Профиль не найден")

    # Update fields
    update_data = profile_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(client, field, value)

    db.commit()
    db.refresh(client)

    return client
