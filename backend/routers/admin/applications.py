from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Application
from schemas.application import ApplicationUpdate, ApplicationResponse

router = APIRouter()


@router.get("/", response_model=List[ApplicationResponse])
async def get_all_applications(
    status: str = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, le=200),
    db: Session = Depends(get_db)
):
    """Get all applications"""
    query = db.query(Application)
    if status:
        query = query.filter(Application.status == status)
    applications = query.offset(skip).limit(limit).all()
    return applications


@router.get("/{application_id}", response_model=ApplicationResponse)
async def get_application(application_id: int, db: Session = Depends(get_db)):
    """Get application by ID"""
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application


@router.put("/{application_id}", response_model=ApplicationResponse)
async def update_application(
    application_id: int,
    application_data: ApplicationUpdate,
    db: Session = Depends(get_db)
):
    """Update application status"""
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    update_data = application_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(application, field, value)

    db.commit()
    db.refresh(application)
    return application
