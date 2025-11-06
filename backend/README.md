# RentFlow Backend

FastAPI backend for RentFlow property rental management system.

## Features

- RESTful API with FastAPI
- PostgreSQL database with SQLAlchemy ORM
- JWT authentication
- Role-based access control
- Comprehensive API documentation (Swagger)
- 50+ API endpoints

## Tech Stack

- **FastAPI 0.104+** - Modern web framework
- **SQLAlchemy 2.0** - ORM
- **PostgreSQL 15** - Database
- **Pydantic V2** - Data validation
- **JWT** - Authentication
- **Alembic** - Database migrations

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env with your settings
```

4. Run the server:
```bash
uvicorn main:app --reload
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Database Migrations

```bash
# Create migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

## Project Structure

```
backend/
├── db/                  # Database
│   ├── database.py     # DB connection
│   ├── models.py       # SQLAlchemy models
│   └── init_data.py    # Initial data
├── schemas/            # Pydantic schemas
├── routers/            # API endpoints
│   ├── client/        # Client APIs
│   ├── employee/      # Employee APIs
│   └── admin/         # Admin APIs
├── utils/             # Utilities
│   ├── security.py    # JWT, hashing
│   ├── validators.py  # Validation
│   └── notifications.py
└── main.py            # Entry point
```

## API Endpoints

### Client APIs
- `POST /api/client/auth/register` - Register
- `POST /api/client/auth/login` - Login
- `GET /api/client/properties` - Browse properties
- `POST /api/client/applications` - Submit application
- `GET /api/client/contracts` - View contracts
- `GET /api/client/payments` - Payment history

### Admin APIs
- `GET /api/admin/statistics/dashboard` - Statistics
- `GET /api/admin/properties` - Manage properties
- `GET /api/admin/applications` - Manage applications
- `GET /api/admin/clients` - Manage clients
- `GET /api/admin/contracts` - Manage contracts

## Testing

```bash
pytest
```

## Deployment

See main README.md for deployment instructions.
