# 🌊 RentFlow - Property Rental Management System

A modern, full-stack property rental management system built with **FastAPI** and **Vue.js 3**.

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 🏠 **Property Management** - Browse, search, and manage rental properties
- 👥 **Client Portal** - User registration, authentication, and profile management
- 📝 **Application System** - Submit and track rental applications
- 📄 **Contract Management** - Digital contracts and agreements
- 💳 **Payment Processing** - Payment tracking and history
- ⭐ **Reviews & Ratings** - Client feedback system
- 🔐 **Admin Panel** - Comprehensive management dashboard
- 🌙 **Dark Theme** - Beautiful dark-themed UI

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern, fast Python web framework
- **SQLAlchemy 2.0** - ORM for database management
- **PostgreSQL** - Relational database
- **Pydantic V2** - Data validation
- **JWT** - Authentication and authorization
- **Alembic** - Database migrations

### Frontend
- **Vue.js 3** - Progressive JavaScript framework
- **Composition API** - Modern Vue development
- **Vue Router 4** - Client-side routing
- **Pinia** - State management
- **Axios** - HTTP client
- **Pure CSS** - No CSS frameworks, custom dark theme
- **Vite** - Fast build tool

## 📁 Project Structure

```
RentFlow/
├── backend/              # FastAPI Backend
│   ├── db/              # Database models and config
│   ├── schemas/         # Pydantic schemas
│   ├── routers/         # API endpoints
│   │   ├── client/     # Client APIs
│   │   ├── employee/   # Employee APIs
│   │   └── admin/      # Admin APIs
│   ├── utils/          # Utilities (security, validators)
│   └── main.py         # Application entry point
│
├── frontend/            # Vue.js Frontend
│   ├── src/
│   │   ├── api/        # API services
│   │   ├── components/ # Vue components
│   │   ├── views/      # Page components
│   │   ├── stores/     # Pinia stores
│   │   ├── router/     # Vue Router config
│   │   └── styles/     # CSS styles (Dark Theme)
│   └── index.html
│
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 15+

### Backend Setup

1. **Navigate to backend directory:**
```bash
cd backend
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment:**
```bash
cp .env.example .env
# Edit .env with your database credentials
```

5. **Run the server:**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`
- **API Docs:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

### Frontend Setup

1. **Navigate to frontend directory:**
```bash
cd frontend
```

2. **Install dependencies:**
```bash
npm install
```

3. **Configure environment:**
```bash
cp .env.example .env
# Edit .env with your API URL
```

4. **Run development server:**
```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

## 📊 Database Schema

The system includes 12 main tables:

1. **user_clients** - Client authentication
2. **positions** - Employee positions
3. **employees** - Employee accounts
4. **companies** - Partner companies
5. **clients** - Client profiles
6. **properties** - Real estate properties
7. **applications** - Rental applications
8. **tenant_verifications** - Tenant background checks
9. **contracts** - Rental contracts
10. **payments** - Payment records
11. **additional_services** - Additional services
12. **reviews** - Client reviews

## 🎨 Design System

The frontend features a **custom dark theme** with:

- **Primary Color:** Blue (#3b82f6)
- **Background:** Dark blue-gray (#0f172a)
- **Components:** Card-based UI with glassmorphism effects
- **Typography:** System fonts for optimal performance
- **Animations:** Smooth transitions and hover effects

## 🔐 Authentication

The system supports two types of authentication:

1. **Client Authentication**
   - Phone-based registration
   - SMS verification
   - JWT token-based sessions

2. **Employee Authentication**
   - Login-based authentication
   - Role-based access control
   - Admin panel access

## 📱 API Endpoints

### Client APIs
- `POST /api/client/auth/register` - Register new client
- `POST /api/client/auth/login` - Client login
- `GET /api/client/properties` - Browse properties
- `POST /api/client/applications` - Submit application
- `GET /api/client/contracts` - View contracts

### Admin APIs
- `GET /api/admin/statistics/dashboard` - Dashboard statistics
- `GET /api/admin/properties` - Manage properties
- `GET /api/admin/applications` - Manage applications
- `GET /api/admin/clients` - Manage clients

Full API documentation available at `/docs`

## 🧪 Development

### Backend Development
```bash
# Run with auto-reload
uvicorn main:app --reload

# Run tests
pytest

# Create migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head
```

### Frontend Development
```bash
# Run dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 📦 Deployment

### Backend Deployment (Render)
1. Create PostgreSQL database on Render
2. Deploy FastAPI app
3. Set environment variables
4. Run migrations

### Frontend Deployment (Netlify)
1. Build the frontend: `npm run build`
2. Deploy `dist/` folder to Netlify
3. Set environment variables
4. Configure redirects for SPA

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License.

## 👥 Team

Developed by **Samolet Plus** team

## 🙏 Acknowledgments

- FastAPI for the amazing Python framework
- Vue.js team for the excellent frontend framework
- PostgreSQL for robust database management

---

**RentFlow** - Modern Property Rental Management 🏢✨
