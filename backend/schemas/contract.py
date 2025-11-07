from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from decimal import Decimal


class ContractCreate(BaseModel):
    contract_number: str
    client_id: int
    property_id: int
    employee_id: Optional[int] = None
    signing_date: date
    start_date: date
    end_date: date
    monthly_rent: Decimal
    deposit_amount: Optional[Decimal] = None
    deposit_paid: bool = False
    payment_day: int = 1
    payment_method: Optional[str] = None
    additional_services: Optional[str] = None


class ContractUpdate(BaseModel):
    contract_status: Optional[str] = None
    payment_method: Optional[str] = None
    additional_services: Optional[str] = None
    termination_date: Optional[date] = None
    termination_reason: Optional[str] = None
    notes: Optional[str] = None


class ContractResponse(BaseModel):
    id: int
    contract_number: str
    client_id: int
    property_id: int
    employee_id: Optional[int] = None
    signing_date: date
    start_date: date
    end_date: date
    monthly_rent: Decimal
    deposit_amount: Optional[Decimal] = None
    deposit_paid: bool
    contract_status: str
    payment_day: int
    payment_method: Optional[str] = None
    additional_services: Optional[str] = None
    contract_file_url: Optional[str] = None
    signed_electronically: bool = False
    termination_date: Optional[date] = None
    termination_reason: Optional[str] = None
    notes: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
