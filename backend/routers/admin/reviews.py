from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Review
from schemas.review import ReviewUpdate, ReviewResponse

router = APIRouter()


@router.get("/", response_model=List[ReviewResponse])
async def get_all_reviews(
    is_approved: bool = None,
    db: Session = Depends(get_db)
):
    """Get all reviews (admin)"""
    query = db.query(Review)

    if is_approved is not None:
        query = query.filter(Review.is_approved == is_approved)

    reviews = query.all()
    return reviews


@router.put("/{review_id}", response_model=ReviewResponse)
async def update_review(
    review_id: int,
    review_data: ReviewUpdate,
    db: Session = Depends(get_db)
):
    """Approve or reject review (admin)"""
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    update_data = review_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(review, field, value)

    db.commit()
    db.refresh(review)

    return review
