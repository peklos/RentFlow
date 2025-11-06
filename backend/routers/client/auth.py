from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import random

from db.database import get_db
from db.models import UserClient, Client
from schemas.user import UserRegister, UserLogin, UserResponse, VerifyPhone
from schemas.client import ClientCreate
from utils.security import get_password_hash, verify_password
from utils.validators import validate_phone, normalize_phone
from utils.notifications import send_verification_code

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserRegister, db: Session = Depends(get_db)):
    """Register a new client"""
    # Validate phone
    if not validate_phone(user_data.phone):
        raise HTTPException(status_code=400, detail="Invalid phone number format")

    # Normalize phone
    normalized_phone = normalize_phone(user_data.phone)

    # Check if user exists
    existing_user = db.query(UserClient).filter(UserClient.phone == normalized_phone).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Phone number already registered")

    # Generate verification code
    verification_code = str(random.randint(100000, 999999))

    # Create user
    new_user = UserClient(
        phone=normalized_phone,
        email=user_data.email,
        password_hash=get_password_hash(user_data.password),
        verification_code=verification_code,
        is_verified=True  # Auto-verify for simplicity
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Create client profile
    new_client = Client(
        user_id=new_user.id,
        full_name=f"Client {new_user.id}",
        phone=normalized_phone,
        email=user_data.email
    )
    db.add(new_client)
    db.commit()

    # Send verification code
    await send_verification_code(normalized_phone, verification_code)

    return new_user


@router.post("/login")
async def login(credentials: UserLogin, db: Session = Depends(get_db)):
    """Login client"""
    normalized_phone = normalize_phone(credentials.phone)

    user = db.query(UserClient).filter(UserClient.phone == normalized_phone).first()
    if not user or not verify_password(credentials.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect phone or password"
        )

    if not user.is_active:
        raise HTTPException(status_code=400, detail="Account is inactive")

    # Return user info instead of token
    return {
        "id": user.id,
        "phone": user.phone,
        "email": user.email,
        "message": "Login successful"
    }


@router.post("/verify-phone", response_model=dict)
async def verify_phone(verify_data: VerifyPhone, db: Session = Depends(get_db)):
    """Verify phone number with code"""
    normalized_phone = normalize_phone(verify_data.phone)

    user = db.query(UserClient).filter(UserClient.phone == normalized_phone).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.verification_code != verify_data.verification_code:
        raise HTTPException(status_code=400, detail="Invalid verification code")

    # Update user
    user.is_verified = True
    user.verification_code = None
    db.commit()

    return {"message": "Phone verified successfully"}


@router.post("/resend-code", response_model=dict)
async def resend_verification_code(phone: str, db: Session = Depends(get_db)):
    """Resend verification code"""
    normalized_phone = normalize_phone(phone)

    user = db.query(UserClient).filter(UserClient.phone == normalized_phone).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.is_verified:
        raise HTTPException(status_code=400, detail="Phone already verified")

    # Generate new code
    verification_code = str(random.randint(100000, 999999))
    user.verification_code = verification_code
    db.commit()

    # Send code
    await send_verification_code(normalized_phone, verification_code)

    return {"message": "Verification code sent"}
