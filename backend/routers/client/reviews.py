from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Review, Client
from schemas.review import ReviewCreate, ReviewResponse
from utils.security import get_current_user

router = APIRouter()


@router.post("/", response_model=ReviewResponse, status_code=201)
async def create_review(
    review_data: ReviewCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new review"""
    if current_user["type"] != "client":
        raise HTTPException(status_code=403, detail="Not authorized")

    client = db.query(Client).filter(Client.user_id == current_user["id"]).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client profile not found")

    new_review = Review(
        client_id=client.id,
        **review_data.dict()
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review


@router.get("/", response_model=List[ReviewResponse])
async def get_my_reviews(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all reviews by current client"""
    if current_user["type"] != "client":
        raise HTTPException(status_code=403, detail="Not authorized")

    client = db.query(Client).filter(Client.user_id == current_user["id"]).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client profile not found")

    reviews = db.query(Review).filter(Review.client_id == client.id).all()
    return reviews
