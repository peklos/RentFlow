from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine, Base, get_db
from db.init_data import create_initial_data

# Import all routers
from routers.client import auth as client_auth
from routers.client import profile, properties, applications, contracts, payments, reviews, services
from routers.employee import auth as employee_auth
from routers.admin import (
    properties as admin_properties,
    applications as admin_applications,
    clients as admin_clients,
    verifications,
    contracts as admin_contracts,
    payments as admin_payments,
    employees as admin_employees,
    positions,
    companies,
    services as admin_services,
    reviews as admin_reviews,
    statistics
)

# Create FastAPI application
app = FastAPI(
    title="RentFlow API",
    description="API for rental property management system - No Auth Version",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware - Allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables and initial data on startup
@app.on_event("startup")
async def startup_event():
    print("🚀 Starting RentFlow API...")
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created")

    # Create initial data
    db = next(get_db())
    try:
        create_initial_data(db)
    except Exception as e:
        print(f"Initial data creation: {e}")
    finally:
        db.close()

# Client routers
app.include_router(client_auth.router, prefix="/api/client/auth", tags=["Client Auth"])
app.include_router(profile.router, prefix="/api/client/profile", tags=["Client Profile"])
app.include_router(properties.router, prefix="/api/client/properties", tags=["Client Properties"])
app.include_router(applications.router, prefix="/api/client/applications", tags=["Client Applications"])
app.include_router(contracts.router, prefix="/api/client/contracts", tags=["Client Contracts"])
app.include_router(payments.router, prefix="/api/client/payments", tags=["Client Payments"])
app.include_router(reviews.router, prefix="/api/client/reviews", tags=["Client Reviews"])
app.include_router(services.router, prefix="/api/client/services", tags=["Client Services"])

# Employee router
app.include_router(employee_auth.router, prefix="/api/employee/auth", tags=["Employee Auth"])

# Admin routers
app.include_router(admin_properties.router, prefix="/api/admin/properties", tags=["Admin Properties"])
app.include_router(admin_applications.router, prefix="/api/admin/applications", tags=["Admin Applications"])
app.include_router(admin_clients.router, prefix="/api/admin/clients", tags=["Admin Clients"])
app.include_router(verifications.router, prefix="/api/admin/verifications", tags=["Admin Verifications"])
app.include_router(admin_contracts.router, prefix="/api/admin/contracts", tags=["Admin Contracts"])
app.include_router(admin_payments.router, prefix="/api/admin/payments", tags=["Admin Payments"])
app.include_router(admin_employees.router, prefix="/api/admin/employees", tags=["Admin Employees"])
app.include_router(positions.router, prefix="/api/admin/positions", tags=["Admin Positions"])
app.include_router(companies.router, prefix="/api/admin/companies", tags=["Admin Companies"])
app.include_router(admin_services.router, prefix="/api/admin/services", tags=["Admin Services"])
app.include_router(admin_reviews.router, prefix="/api/admin/reviews", tags=["Admin Reviews"])
app.include_router(statistics.router, prefix="/api/admin/statistics", tags=["Admin Statistics"])

# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to RentFlow API",
        "version": "2.0.0",
        "status": "operational",
        "docs": "/docs",
        "redoc": "/redoc",
        "features": [
            "50+ API endpoints",
            "12 database tables",
            "No authentication required",
            "Full CRUD operations",
            "Test data included"
        ]
    }

# Health check endpoints for uptime monitoring
@app.get("/health")
@app.head("/health")
def health_check():
    return {"status": "healthy", "service": "RentFlow API v2.0"}
