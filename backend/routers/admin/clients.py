from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Client
from schemas.client import ClientResponse

router = APIRouter()


@router.get("/", response_model=List[ClientResponse])
async def get_all_clients(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, le=100),
    db: Session = Depends(get_db)
):
    """Get all clients (admin)"""
    clients = db.query(Client).offset(skip).limit(limit).all()
    return clients


@router.get("/{client_id}", response_model=ClientResponse)
async def get_client(
    client_id: int,
    db: Session = Depends(get_db)
):
    """Get client by ID (admin)"""
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Клиент не найден")

    return client
