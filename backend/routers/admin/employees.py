from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import Employee
from schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from utils.security import require_role, get_password_hash

router = APIRouter()


@router.post("/", response_model=EmployeeResponse, status_code=201)
async def create_employee(
    employee_data: EmployeeCreate,
    current_user: dict = Depends(require_role("employee")),
    db: Session = Depends(get_db)
):
    """Create a new employee (admin)"""
    # Check if login already exists
    existing = db.query(Employee).filter(Employee.login == employee_data.login).first()
    if existing:
        raise HTTPException(status_code=400, detail="Login already exists")

    employee_dict = employee_data.dict()
    password = employee_dict.pop("password")
    employee_dict["password_hash"] = get_password_hash(password)

    new_employee = Employee(**employee_dict)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee


@router.get("/", response_model=List[EmployeeResponse])
async def get_all_employees(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, le=100),
    current_user: dict = Depends(require_role("employee")),
    db: Session = Depends(get_db)
):
    """Get all employees (admin)"""
    employees = db.query(Employee).offset(skip).limit(limit).all()
    return employees
