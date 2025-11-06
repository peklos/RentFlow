from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import get_db
from db.models import Employee
from schemas.employee import EmployeeLogin

router = APIRouter()


@router.post("/login")
async def employee_login(credentials: EmployeeLogin, db: Session = Depends(get_db)):
    """Login for employees (plain password for educational purposes)"""
    employee = db.query(Employee).filter(Employee.login == credentials.login).first()

    if not employee or credentials.password != employee.password_hash:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password"
        )

    if not employee.is_active:
        raise HTTPException(status_code=400, detail="Employee account is inactive")

    # Return employee info instead of token
    return {
        "id": employee.id,
        "login": employee.login,
        "position_id": employee.position_id,
        "message": "Login successful"
    }
