# 🌊 RentFlow - Property Rental Management System

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Vue](https://img.shields.io/badge/vue-3.3-green.svg)

A modern, full-stack property rental management system with **dark theme UI** and **complete test data**.

**✅ No Authentication Required** - Ready for demo and testing!

---

## ✨ Features

- 🏠 **Property Management** - 8 pre-loaded properties (residential & commercial)
- 👥 **Client Management** - Complete client profiles with test data
- 📝 **Application System** - Submit and track rental applications
- 📄 **Contract Management** - Digital contracts with payment tracking
- 💳 **Payment System** - Payment history and tracking
- ⭐ **Reviews & Ratings** - Client feedback system
- 🔐 **Admin Panel** - Dashboard with real-time statistics
- 🌙 **Beautiful Dark Theme** - Modern, responsive UI
- 🚀 **Ready to Deploy** - Configured for Render + Netlify + Neon

---

## 🛠️ Technology Stack

### Backend
- **FastAPI 0.104** - High-performance Python web framework
- **SQLAlchemy 2.0** - Modern ORM
- **PostgreSQL 15** - Production database
- **Pydantic V2** - Data validation
- **Uvicorn** - ASGI server
- **50+ API Endpoints** - Full REST API

### Frontend
- **Vue.js 3** - Progressive framework with Composition API
- **Pinia** - State management
- **Vue Router 4** - Client-side routing
- **Axios** - HTTP client
- **Pure CSS** - Custom dark theme (no frameworks)
- **Vite** - Lightning-fast build tool

### Database
- **12 Tables** - Complete data model
- **Test Data Included** - 8 properties, 3 clients, contracts, payments, reviews
- **Auto-initialization** - Data created on first startup

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 15+ (or use Docker)

### 1. Clone Repository

```bash
git clone https://github.com/peklos/RentFlow.git
cd RentFlow
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure database
cp .env.example .env
# Edit .env with your PostgreSQL connection string

# Start server
uvicorn main:app --reload
```

**Backend will be available at:** http://localhost:8000

**API Documentation:** http://localhost:8000/docs

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Configure API URL
cp .env.example .env
# VITE_API_BASE_URL=http://localhost:8000/api

# Start development server
npm run dev
```

**Frontend will be available at:** http://localhost:5173

---

## 📊 Test Data

The system includes pre-loaded test data:

### 🏢 Properties
- 8 properties (6 residential, 2 commercial)
- Various locations in Moscow
- Different price ranges (45,000₽ - 500,000₽/month)
- All with detailed descriptions and amenities

### 👤 Test Accounts

**Employees:**
- **Admin:** `login: admin`, `password: admin123`
- **Manager:** `login: manager1`, `password: manager123`

**Clients:**
- **Client 1:** `phone: +79998887766`, `password: client123`
- **Client 2:** `phone: +79997776655`, `password: client123`
- **Client 3:** `phone: +79996665544`, `password: client123`

### 📈 Pre-loaded Data
- ✅ 3 Applications (different statuses)
- ✅ 1 Active Contract
- ✅ 2 Completed Payments
- ✅ 3 Reviews (all approved)
- ✅ 4 Additional Services

---

## 📡 API Endpoints

**Total:** 54+ endpoints

### Client APIs
- `POST /api/client/auth/register` - Register
- `POST /api/client/auth/login` - Login
- `GET /api/client/properties` - Browse properties
- `POST /api/client/applications` - Submit application
- `GET /api/client/contracts` - View contracts
- `GET /api/client/payments` - Payment history

### Admin APIs
- `GET /api/admin/statistics/dashboard` - Dashboard stats
- `POST /api/admin/properties` - Create property
- `GET /api/admin/applications` - Manage applications
- `GET /api/admin/clients` - Manage clients
- `PUT /api/admin/contracts/{id}` - Update contract

**📖 Full API documentation:** [API_ENDPOINTS.md](./API_ENDPOINTS.md)

---

## 🌙 Dark Theme

Custom-designed dark theme with:
- **Primary:** Blue (#3b82f6) with glow effects
- **Background:** Dark blue-gray (#0f172a)
- **Components:** Glassmorphism with shadows
- **Animations:** Smooth transitions
- **Responsive:** Mobile-friendly design

---

## 📁 Project Structure

```
RentFlow/
├── backend/              # FastAPI Backend
│   ├── db/              # Database models & init data
│   ├── schemas/         # Pydantic schemas (12)
│   ├── routers/         # API endpoints (54+)
│   │   ├── client/     # Client APIs (8 files)
│   │   ├── employee/   # Employee APIs
│   │   └── admin/      # Admin APIs (13 files)
│   ├── utils/          # Utilities
│   └── main.py         # App entry point
│
├── frontend/            # Vue.js Frontend
│   ├── src/
│   │   ├── api/        # API services
│   │   ├── components/ # Vue components
│   │   ├── views/      # Pages (15+)
│   │   ├── stores/     # Pinia stores (4)
│   │   ├── router/     # Vue Router
│   │   └── styles/     # Dark theme CSS
│   └── index.html
│
├── render.yaml          # Render deployment config
├── DEPLOYMENT.md        # Deployment guide
└── API_ENDPOINTS.md     # API documentation
```

---

## 🚀 Deployment

Deploy to production in minutes!

### Stack
- **Backend:** Render.com (free tier)
- **Frontend:** Netlify (free tier)
- **Database:** Neon.tech PostgreSQL (free tier)

### Quick Deploy

**1. Database (Neon):**
- Create project at [neon.tech](https://neon.tech)
- Copy connection string

**2. Backend (Render):**
- Connect GitHub repository
- Use `render.yaml` configuration
- Add `DATABASE_URL` environment variable

**3. Frontend (Netlify):**
- Connect GitHub repository
- Use `netlify.toml` configuration
- Set `VITE_API_BASE_URL` to your Render URL

**📖 Full deployment guide:** [DEPLOYMENT.md](./DEPLOYMENT.md)

---

## 🧪 Testing

### Using cURL

```bash
# Get all properties
curl http://localhost:8000/api/client/properties

# Get dashboard statistics
curl http://localhost:8000/api/admin/statistics/dashboard

# Create application
curl -X POST http://localhost:8000/api/client/applications \
  -H "Content-Type: application/json" \
  -d '{"client_id":1,"property_id":1,"lease_duration_months":12}'
```

### Using Browser

1. Open http://localhost:5173
2. Browse properties
3. View dashboard at http://localhost:5173/admin/dashboard
4. Try login with test credentials

### Using Swagger UI

Visit http://localhost:8000/docs for interactive API testing

---

## 📊 Database Schema

**12 Tables:**
1. `user_clients` - Authentication
2. `positions` - Employee positions
3. `employees` - Staff accounts
4. `companies` - Partner companies
5. `clients` - Client profiles
6. `properties` - Real estate
7. `applications` - Rental applications
8. `tenant_verifications` - Background checks
9. `contracts` - Rental agreements
10. `payments` - Payment records
11. `additional_services` - Extra services
12. `reviews` - Client feedback

---

## 🔥 Key Features

### ✅ No Authentication
- JWT completely removed
- All endpoints accessible
- Perfect for demo and testing

### ✅ Complete Test Data
- Automatically populated on startup
- Real-world scenarios
- Ready for immediate testing

### ✅ Production Ready
- Full CRUD operations
- Error handling
- Data validation
- CORS configured
- Deployment ready

### ✅ Beautiful UI
- Modern dark theme
- Responsive design
- Smooth animations
- Intuitive navigation

---

## 📚 Documentation

- **[API Endpoints](./API_ENDPOINTS.md)** - Complete API reference
- **[Deployment Guide](./DEPLOYMENT.md)** - Step-by-step deployment
- **[Backend README](./backend/README.md)** - Backend documentation
- **[Frontend README](./frontend/README.md)** - Frontend documentation

---

## 🛠️ Development

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Docker

```bash
docker-compose up
```

---

## 📈 Statistics

- **Lines of Code:** 5000+
- **API Endpoints:** 54+
- **Vue Components:** 20+
- **Database Tables:** 12
- **Test Records:** 50+

---

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📝 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- **Samolet Plus** - Project sponsor
- **FastAPI** - Amazing Python framework
- **Vue.js** - Excellent frontend framework
- **PostgreSQL** - Robust database

---

## 📞 Support

- **Documentation:** Check `/docs` endpoint
- **Issues:** Create GitHub issue
- **API Docs:** http://localhost:8000/docs

---

## 🎯 Roadmap

- [ ] Add real-time notifications
- [ ] Implement payment gateway
- [ ] Add property map view
- [ ] Mobile app (React Native)
- [ ] Advanced search filters
- [ ] Multi-language support

---

**RentFlow v2.0** - Modern Property Rental Management 🏢✨

Made with ❤️ by Samolet Plus Team

🌊 **Ready to Deploy | No Auth Required | Dark Theme | Full Test Data**
