# 📡 RentFlow API Endpoints

Complete list of all 50+ API endpoints available in RentFlow v2.0

**Base URL:** `http://localhost:8000/api` (local) or `https://your-app.onrender.com/api` (production)

**Authentication:** ❌ No authentication required (tokens removed for demo)

---

## 🏠 Client APIs

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/client/auth/register` | Register new client |
| `POST` | `/client/auth/login` | Login client |
| `POST` | `/client/auth/verify-phone` | Verify phone with code |
| `POST` | `/client/auth/resend-code` | Resend verification code |

### Profile

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/client/profile/{client_id}` | Get profile by ID |
| `GET` | `/client/profile/` | Get all profiles |
| `PUT` | `/client/profile/{client_id}` | Update profile |

### Properties

| Method | Endpoint | Description | Query Params |
|--------|----------|-------------|--------------|
| `GET` | `/client/properties` | Browse properties | `type`, `min_price`, `max_price`, `min_area`, `max_area`, `rooms_count`, `is_furnished`, `status`, `skip`, `limit` |
| `GET` | `/client/properties/{id}` | Get property details | - |

### Applications

| Method | Endpoint | Description | Query Params |
|--------|----------|-------------|--------------|
| `POST` | `/client/applications` | Submit application | - |
| `GET` | `/client/applications` | Get applications | `client_id`, `skip`, `limit` |
| `GET` | `/client/applications/{id}` | Get application details | - |

### Contracts

| Method | Endpoint | Description | Query Params |
|--------|----------|-------------|--------------|
| `GET` | `/client/contracts` | Get contracts | `client_id`, `skip`, `limit` |
| `GET` | `/client/contracts/{id}` | Get contract details | - |

### Payments

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/client/payments` | Get payment history |

### Reviews

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/client/reviews` | Create review |
| `GET` | `/client/reviews` | Get reviews |

### Services

| Method | Endpoint | Description | Query Params |
|--------|----------|-------------|--------------|
| `GET` | `/client/services` | Get additional services | `is_active`, `skip`, `limit` |

---

## 👔 Employee APIs

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/employee/auth/login` | Employee login |

---

## 🔧 Admin APIs

### Properties Management

| Method | Endpoint | Description | Query Params |
|--------|----------|-------------|--------------|
| `POST` | `/admin/properties` | Create property | - |
| `GET` | `/admin/properties` | Get all properties | `skip`, `limit` |
| `GET` | `/admin/properties/{id}` | Get property by ID | - |
| `PUT` | `/admin/properties/{id}` | Update property | - |
| `DELETE` | `/admin/properties/{id}` | Delete property | - |

### Applications Management

| Method | Endpoint | Description | Query Params |
|--------|----------|-------------|--------------|
| `GET` | `/admin/applications` | Get all applications | `status`, `skip`, `limit` |
| `GET` | `/admin/applications/{id}` | Get application by ID | - |
| `PUT` | `/admin/applications/{id}` | Update application | - |

### Clients Management

| Method | Endpoint | Description | Query Params |
|--------|----------|-------------|--------------|
| `GET` | `/admin/clients` | Get all clients | `skip`, `limit` |
| `GET` | `/admin/clients/{id}` | Get client by ID | - |

### Verifications Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/admin/verifications` | Create verification |
| `GET` | `/admin/verifications` | Get all verifications |

### Contracts Management

| Method | Endpoint | Description | Query Params |
|--------|----------|-------------|--------------|
| `POST` | `/admin/contracts` | Create contract | - |
| `GET` | `/admin/contracts` | Get all contracts | `status`, `skip`, `limit` |
| `PUT` | `/admin/contracts/{id}` | Update contract | - |

### Payments Management

| Method | Endpoint | Description | Query Params |
|--------|----------|-------------|--------------|
| `GET` | `/admin/payments` | Get all payments | `status`, `skip`, `limit` |
| `PUT` | `/admin/payments/{id}` | Update payment | - |

### Employees Management

| Method | Endpoint | Description | Query Params |
|--------|----------|-------------|--------------|
| `POST` | `/admin/employees` | Create employee | - |
| `GET` | `/admin/employees` | Get all employees | `skip`, `limit` |

### Positions Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/admin/positions` | Create position |
| `GET` | `/admin/positions` | Get all positions |

### Companies Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/admin/companies` | Create company |
| `GET` | `/admin/companies` | Get all companies |

### Services Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/admin/services` | Create service |
| `GET` | `/admin/services` | Get all services |
| `PUT` | `/admin/services/{id}` | Update service |

### Reviews Management

| Method | Endpoint | Description | Query Params |
|--------|----------|-------------|--------------|
| `GET` | `/admin/reviews` | Get all reviews | `is_approved` |
| `PUT` | `/admin/reviews/{id}` | Approve/reject review | - |

### Statistics

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/admin/statistics/dashboard` | Get dashboard statistics |

---

## 📊 Response Examples

### Get Properties
```bash
GET /api/client/properties?type=residential&max_price=100000&skip=0&limit=10
```

**Response:**
```json
[
  {
    "id": 1,
    "type": "residential",
    "subtype": "Apartment",
    "address": "Moscow, Arbat Street, 15, apt 42",
    "area": "75.5",
    "rooms_count": 2,
    "floor": 5,
    "total_floors": 12,
    "monthly_rent": "80000",
    "status": "available",
    "description": "Cozy 2-room apartment...",
    "amenities": "Wi-Fi, Air conditioning...",
    "created_at": "2024-01-01T00:00:00"
  }
]
```

### Dashboard Statistics
```bash
GET /api/admin/statistics/dashboard
```

**Response:**
```json
{
  "properties": {
    "total": 8,
    "available": 7,
    "rented": 1
  },
  "clients": {
    "total": 3,
    "verified": 3
  },
  "contracts": {
    "total": 1,
    "active": 1
  },
  "applications": {
    "total": 3,
    "pending": 1
  },
  "revenue": {
    "total": 130000.0
  }
}
```

### Create Application
```bash
POST /api/client/applications
Content-Type: application/json

{
  "client_id": 1,
  "property_id": 1,
  "preferred_move_in_date": "2024-12-01",
  "lease_duration_months": 12,
  "notes": "Looking for long-term rental"
}
```

**Response:**
```json
{
  "id": 4,
  "client_id": 1,
  "property_id": 1,
  "application_date": "2024-11-06",
  "status": "pending",
  "preferred_move_in_date": "2024-12-01",
  "lease_duration_months": 12,
  "notes": "Looking for long-term rental",
  "created_at": "2024-11-06T10:30:00"
}
```

---

## 🧪 Testing Endpoints

### Using cURL

```bash
# Get all properties
curl http://localhost:8000/api/client/properties

# Get property by ID
curl http://localhost:8000/api/client/properties/1

# Create application
curl -X POST http://localhost:8000/api/client/applications \
  -H "Content-Type: application/json" \
  -d '{"client_id":1,"property_id":1,"lease_duration_months":12}'

# Get dashboard statistics
curl http://localhost:8000/api/admin/statistics/dashboard
```

### Using JavaScript (Axios)

```javascript
import axios from 'axios'

const API_URL = 'http://localhost:8000/api'

// Get properties
const properties = await axios.get(`${API_URL}/client/properties`, {
  params: { type: 'residential', max_price: 100000 }
})

// Create application
const application = await axios.post(`${API_URL}/client/applications`, {
  client_id: 1,
  property_id: 1,
  lease_duration_months: 12
})

// Get statistics
const stats = await axios.get(`${API_URL}/admin/statistics/dashboard`)
```

### Using Python (requests)

```python
import requests

API_URL = 'http://localhost:8000/api'

# Get properties
response = requests.get(f'{API_URL}/client/properties', params={
    'type': 'residential',
    'max_price': 100000
})
properties = response.json()

# Create application
response = requests.post(f'{API_URL}/client/applications', json={
    'client_id': 1,
    'property_id': 1,
    'lease_duration_months': 12
})
application = response.json()
```

---

## 📝 Notes

- All endpoints return JSON responses
- Timestamps are in ISO 8601 format
- Pagination uses `skip` and `limit` query parameters
- Default `limit` is 50, maximum is 200
- All decimal values (prices, areas) are returned as strings
- Error responses include `detail` field with error message

---

## 🚀 Interactive Documentation

Visit `/docs` endpoint for interactive Swagger UI:

**Local:** http://localhost:8000/docs
**Production:** https://your-app.onrender.com/docs

---

**Total Endpoints:** 54+
**Database Tables:** 12
**Test Data:** Included automatically on first startup

🌊 RentFlow API v2.0 - No Auth Required!
