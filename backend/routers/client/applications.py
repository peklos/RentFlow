from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Application
from schemas.application import ApplicationCreate, ApplicationResponse

router = APIRouter()


@router.post("/", response_model=ApplicationResponse, status_code=201)
async def create_application(
    application_data: ApplicationCreate,
    db: Session = Depends(get_db)
):
    """Create a new rental application"""
    new_application = Application(**application_data.dict())
    db.add(new_application)
    db.commit()
    db.refresh(new_application)
    return new_application


@router.get("/", response_model=List[ApplicationResponse])
async def get_applications(
    client_id: int = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(50, le=100),
    db: Session = Depends(get_db)
):
    """Get all applications (optionally filtered by client_id)"""
    query = db.query(Application)
    if client_id:
        query = query.filter(Application.client_id == client_id)
    applications = query.offset(skip).limit(limit).all()
    return applications


@router.get("/{application_id}", response_model=ApplicationResponse)
async def get_application(application_id: int, db: Session = Depends(get_db)):
    """Get specific application"""
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Заявка не найдена")
    return application
