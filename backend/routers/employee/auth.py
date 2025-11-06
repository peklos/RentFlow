from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta

from db.database import get_db
from db.models import Employee
from schemas.employee import EmployeeLogin
from schemas.user import Token
from utils.security import verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()


@router.post("/login", response_model=Token)
async def employee_login(credentials: EmployeeLogin, db: Session = Depends(get_db)):
    """Login for employees"""
    employee = db.query(Employee).filter(Employee.login == credentials.login).first()

    if not employee or not verify_password(credentials.password, employee.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password"
        )

    if not employee.is_active:
        raise HTTPException(status_code=400, detail="Employee account is inactive")

    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(employee.id), "type": "employee"},
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
