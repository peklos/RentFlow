from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Application, Client
from schemas.application import ApplicationCreate, ApplicationResponse
from utils.security import get_current_user

router = APIRouter()


@router.post("/", response_model=ApplicationResponse, status_code=201)
async def create_application(
    application_data: ApplicationCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new rental application"""
    if current_user["type"] != "client":
        raise HTTPException(status_code=403, detail="Not authorized")

    # Get client profile
    client = db.query(Client).filter(Client.user_id == current_user["id"]).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client profile not found")

    # Create application
    new_application = Application(
        client_id=client.id,
        **application_data.dict()
    )

    db.add(new_application)
    db.commit()
    db.refresh(new_application)

    return new_application


@router.get("/", response_model=List[ApplicationResponse])
async def get_my_applications(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all applications for current client"""
    if current_user["type"] != "client":
        raise HTTPException(status_code=403, detail="Not authorized")

    client = db.query(Client).filter(Client.user_id == current_user["id"]).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client profile not found")

    applications = db.query(Application).filter(Application.client_id == client.id).all()
    return applications


@router.get("/{application_id}", response_model=ApplicationResponse)
async def get_application(
    application_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get specific application details"""
    if current_user["type"] != "client":
        raise HTTPException(status_code=403, detail="Not authorized")

    client = db.query(Client).filter(Client.user_id == current_user["id"]).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client profile not found")

    application = db.query(Application).filter(
        Application.id == application_id,
        Application.client_id == client.id
    ).first()

    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    return application
