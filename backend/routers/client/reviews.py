from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Review, Client
from schemas.review import ReviewCreate, ReviewResponse

router = APIRouter()


@router.post("/", response_model=ReviewResponse, status_code=201)
async def create_review(
    review_data: ReviewCreate,
    db: Session = Depends(get_db)
):
    """Create a new review (authentication removed)"""
    # Create review with provided client_id (no authentication check)
    new_review = Review(**review_data.dict())

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review


@router.get("/", response_model=List[ReviewResponse])
async def get_my_reviews(
    db: Session = Depends(get_db)
):
    """Get all reviews (authentication removed)"""
    # Return all reviews (no user filtering since JWT was removed)
    reviews = db.query(Review).all()
    return reviews
