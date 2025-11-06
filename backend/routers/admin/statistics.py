from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from db.database import get_db
from db.models import Property, Client, Contract, Payment, Application

router = APIRouter()


@router.get("/dashboard")
async def get_dashboard_statistics(
    db: Session = Depends(get_db)
):
    """Get dashboard statistics (admin)"""

    total_properties = db.query(func.count(Property.id)).scalar()
    available_properties = db.query(func.count(Property.id)).filter(
        Property.status == "available"
    ).scalar()

    total_clients = db.query(func.count(Client.id)).scalar()
    verified_clients = db.query(func.count(Client.id)).filter(
        Client.is_verified == True
    ).scalar()

    total_contracts = db.query(func.count(Contract.id)).scalar()
    active_contracts = db.query(func.count(Contract.id)).filter(
        Contract.contract_status == "active"
    ).scalar()

    total_applications = db.query(func.count(Application.id)).scalar()
    pending_applications = db.query(func.count(Application.id)).filter(
        Application.status == "pending"
    ).scalar()

    total_revenue = db.query(func.sum(Payment.amount)).filter(
        Payment.payment_status == "completed"
    ).scalar() or 0

    return {
        "properties": {
            "total": total_properties,
            "available": available_properties,
            "rented": total_properties - available_properties
        },
        "clients": {
            "total": total_clients,
            "verified": verified_clients
        },
        "contracts": {
            "total": total_contracts,
            "active": active_contracts
        },
        "applications": {
            "total": total_applications,
            "pending": pending_applications
        },
        "revenue": {
            "total": float(total_revenue)
        }
    }
