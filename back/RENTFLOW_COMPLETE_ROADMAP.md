# 🌊 ПОЛНЫЙ РОАДМАП ПРОЕКТА "RENTFLOW"
## Система управления арендой недвижимости - Готово к реализации в Claude Code

---

## 📋 КРАТКОЕ РЕЗЮМЕ

**Название проекта:** RentFlow  
**Компания:** ООО «Самолет Плюс»  
**Стек:** FastAPI + Vue.js 3 + PostgreSQL + Pure CSS (CSS Modules)  
**Срок разработки:** 40-55 рабочих дней  
**Таблиц БД:** 12 основных таблиц  
**API эндпоинтов:** 50+ эндпоинтов  
**Страниц:** 40+ страниц  
**Особенность:** Полная спецификация для реализации в Claude Code

---

## 🎯 ТЕХНОЛОГИЧЕСКИЙ СТЕК (БЕЗ ФРЕЙМВОРКОВ CSS)

### Backend:
- **Python 3.11+**
- **FastAPI 0.104+** - веб-фреймворк
- **SQLAlchemy 2.0** - ORM
- **PostgreSQL 15** - база данных
- **Alembic** - миграции БД
- **Pydantic V2** - валидация данных
- **python-jose** - JWT токены
- **passlib[bcrypt]** - хэширование паролей
- **python-multipart** - загрузка файлов
- **uvicorn** - ASGI сервер

### Frontend:
- **Vue.js 3** - Composition API
- **Vue Router 4** - маршрутизация
- **Pinia** - state management
- **Axios** - HTTP клиент
- **Pure CSS** - чистые CSS стили
- **CSS Modules** - изолированные стили
- **Vite** - сборщик

### Database:
- **PostgreSQL 15**
- **12 таблиц** с полными связями
- **Индексы** для оптимизации
- **Foreign Keys** для целостности

### Deployment:
- **Render.com** - бэкенд + PostgreSQL
- **Netlify** - фронтенд
- **Docker** - локальная разработка

---

## 📁 СТРУКТУРА ПРОЕКТА (ДЛЯ РЕАЛИЗАЦИИ)

```
RentFlow/
│
├── backend/                          # БЭКЕНД НА FASTAPI
│   │
│   ├── db/                          # База данных
│   │   ├── __init__.py
│   │   ├── database.py              # Подключение к PostgreSQL
│   │   ├── models.py                # 12 моделей SQLAlchemy
│   │   └── init_data.py             # Начальные данные (должности, тестовые данные)
│   │
│   ├── schemas/                     # Pydantic схемы (валидация)
│   │   ├── __init__.py
│   │   ├── user.py                  # UserRegister, UserLogin, UserResponse
│   │   ├── client.py                # ClientCreate, ClientUpdate, ClientProfile
│   │   ├── property.py              # PropertyCreate, PropertyUpdate, PropertyResponse, PropertyFilter
│   │   ├── application.py           # ApplicationCreate, ApplicationUpdate, ApplicationResponse
│   │   ├── contract.py              # ContractCreate, ContractUpdate, ContractResponse
│   │   ├── payment.py               # PaymentCreate, PaymentUpdate, PaymentResponse
│   │   ├── verification.py          # VerificationCreate, VerificationUpdate
│   │   ├── employee.py              # EmployeeCreate, EmployeeUpdate
│   │   ├── position.py              # PositionCreate, PositionUpdate
│   │   ├── company.py               # CompanyCreate, CompanyUpdate
│   │   ├── service.py               # ServiceCreate, ServiceUpdate
│   │   └── review.py                # ReviewCreate, ReviewUpdate
│   │
│   ├── routers/                     # API эндпоинты
│   │   │
│   │   ├── client/                  # Клиентские API
│   │   │   ├── __init__.py
│   │   │   ├── auth.py              # POST /register, /login, /verify-phone
│   │   │   ├── profile.py           # GET/PUT /profile/me
│   │   │   ├── properties.py        # GET /properties (с фильтрами)
│   │   │   ├── applications.py      # POST/GET /applications
│   │   │   ├── contracts.py         # GET /contracts
│   │   │   ├── payments.py          # GET/POST /payments
│   │   │   ├── reviews.py           # POST/GET /reviews
│   │   │   └── services.py          # GET /services
│   │   │
│   │   ├── employee/                # Авторизация сотрудников
│   │   │   ├── __init__.py
│   │   │   └── auth.py              # POST /login
│   │   │
│   │   └── admin/                   # Админские API
│   │       ├── __init__.py
│   │       ├── properties.py        # CRUD объектов
│   │       ├── applications.py      # Управление заявками
│   │       ├── clients.py           # Управление клиентами
│   │       ├── verifications.py     # Проверка арендаторов
│   │       ├── contracts.py         # Управление договорами
│   │       ├── payments.py          # Управление платежами
│   │       ├── employees.py         # Управление сотрудниками
│   │       ├── positions.py         # Должности
│   │       ├── companies.py         # Компании
│   │       ├── services.py          # Доп.услуги
│   │       ├── reviews.py           # Модерация отзывов
│   │       └── statistics.py        # Статистика и отчеты
│   │
│   ├── utils/                       # Утилиты
│   │   ├── __init__.py
│   │   ├── security.py              # JWT, хэширование паролей, get_current_user
│   │   ├── validators.py            # Валидация телефона, email, паспорта
│   │   ├── notifications.py         # Отправка SMS/Email
│   │   └── file_upload.py           # Загрузка файлов (фото, документы)
│   │
│   ├── main.py                      # Главный файл приложения
│   ├── requirements.txt             # Зависимости Python
│   ├── .env.example                 # Пример переменных окружения
│   ├── Dockerfile                   # Docker для бэкенда
│   └── README.md                    # Документация бэкенда
│
│
├── frontend/                         # ФРОНТЕНД НА VUE.JS 3
│   │
│   ├── public/
│   │   ├── favicon.ico
│   │   └── logo.png
│   │
│   ├── src/
│   │   │
│   │   ├── api/                     # API клиент
│   │   │   ├── axios.js             # Настройка axios (baseURL, interceptors)
│   │   │   └── services/            # API сервисы
│   │   │       ├── auth.js          # authAPI.login(), register(), verify()
│   │   │       ├── properties.js    # propertiesAPI.getAll(), getById()
│   │   │       ├── applications.js  # applicationsAPI.create(), getAll()
│   │   │       ├── contracts.js     # contractsAPI.getAll(), getById()
│   │   │       ├── payments.js      # paymentsAPI.getAll(), create()
│   │   │       ├── clients.js       # clientsAPI (для админа)
│   │   │       ├── employees.js     # employeesAPI (для админа)
│   │   │       └── admin.js         # adminAPI.getStatistics()
│   │   │
│   │   ├── assets/                  # Статические файлы
│   │   │   ├── images/
│   │   │   └── icons/
│   │   │
│   │   ├── components/              # Компоненты Vue
│   │   │   │
│   │   │   ├── common/              # Общие UI компоненты
│   │   │   │   ├── BaseButton.vue           # <BaseButton>
│   │   │   │   ├── BaseInput.vue            # <BaseInput>
│   │   │   │   ├── BaseCard.vue             # <BaseCard>
│   │   │   │   ├── BaseModal.vue            # <BaseModal>
│   │   │   │   ├── BaseLoader.vue           # <BaseLoader>
│   │   │   │   ├── BasePagination.vue       # <BasePagination>
│   │   │   │   └── BaseTable.vue            # <BaseTable>
│   │   │   │
│   │   │   ├── layout/              # Компоненты макета
│   │   │   │   ├── AppHeader.vue            # Шапка сайта
│   │   │   │   ├── AppFooter.vue            # Подвал
│   │   │   │   ├── ClientSidebar.vue        # Сайдбар клиента (для ЛК)
│   │   │   │   └── AdminSidebar.vue         # Сайдбар админа
│   │   │   │
│   │   │   ├── property/            # Компоненты объектов
│   │   │   │   ├── PropertyCard.vue         # Карточка объекта
│   │   │   │   ├── PropertyFilter.vue       # Фильтр объектов
│   │   │   │   ├── PropertyGallery.vue      # Галерея фото
│   │   │   │   └── PropertyForm.vue         # Форма создания/редактирования
│   │   │   │
│   │   │   ├── application/         # Компоненты заявок
│   │   │   │   ├── ApplicationCard.vue      # Карточка заявки
│   │   │   │   ├── ApplicationForm.vue      # Форма подачи заявки
│   │   │   │   └── ApplicationStatus.vue    # Статус заявки (бейдж)
│   │   │   │
│   │   │   ├── contract/            # Компоненты договоров
│   │   │   │   ├── ContractCard.vue         # Карточка договора
│   │   │   │   ├── ContractDetail.vue       # Детали договора
│   │   │   │   └── ContractForm.vue         # Форма создания договора
│   │   │   │
│   │   │   └── admin/               # Админские компоненты
│   │   │       ├── StatCard.vue             # Карточка статистики
│   │   │       ├── DataTable.vue            # Универсальная таблица
│   │   │       └── FilterPanel.vue          # Панель фильтров
│   │   │
│   │   ├── views/                   # Страницы (Views)
│   │   │   │
│   │   │   ├── client/              # Клиентские страницы
│   │   │   │   ├── HomePage.vue              # Главная страница
│   │   │   │   ├── PropertiesPage.vue        # Каталог объектов
│   │   │   │   ├── PropertyDetailPage.vue    # Детальная страница объекта
│   │   │   │   ├── ProfilePage.vue           # Личный кабинет
│   │   │   │   ├── ApplicationsPage.vue      # Мои заявки
│   │   │   │   ├── ContractsPage.vue         # Мои договоры
│   │   │   │   ├── PaymentsPage.vue          # История платежей
│   │   │   │   └── ReviewsPage.vue           # Мои отзывы
│   │   │   │
│   │   │   ├── auth/                # Страницы авторизации
│   │   │   │   ├── ClientLoginPage.vue       # Вход клиента
│   │   │   │   ├── ClientRegisterPage.vue    # Регистрация клиента
│   │   │   │   ├── EmployeeLoginPage.vue     # Вход сотрудника
│   │   │   │   └── VerifyPhonePage.vue       # Подтверждение телефона
│   │   │   │
│   │   │   └── admin/               # Админские страницы
│   │   │       ├── DashboardPage.vue         # Главная админки (статистика)
│   │   │       ├── PropertiesManagePage.vue  # Управление объектами
│   │   │       ├── ApplicationsManagePage.vue # Управление заявками
│   │   │       ├── ClientsManagePage.vue     # Управление клиентами
│   │   │       ├── VerificationsManagePage.vue # Проверка арендаторов
│   │   │       ├── ContractsManagePage.vue   # Управление договорами
│   │   │       ├── PaymentsManagePage.vue    # Управление платежами
│   │   │       ├── EmployeesManagePage.vue   # Управление персоналом
│   │   │       ├── PositionsManagePage.vue   # Должности
│   │   │       ├── CompaniesManagePage.vue   # Компании
│   │   │       ├── ServicesManagePage.vue    # Доп.услуги
│   │   │       ├── ReviewsManagePage.vue     # Модерация отзывов
│   │   │       └── StatisticsPage.vue        # Статистика и отчеты
│   │   │
│   │   ├── stores/                  # Pinia Stores
│   │   │   ├── auth.js              # useAuthStore - авторизация
│   │   │   ├── properties.js        # usePropertiesStore - объекты
│   │   │   ├── applications.js      # useApplicationsStore - заявки
│   │   │   ├── contracts.js         # useContractsStore - договоры
│   │   │   ├── payments.js          # usePaymentsStore - платежи
│   │   │   ├── clients.js           # useClientsStore - клиенты (админ)
│   │   │   ├── employees.js         # useEmployeesStore - сотрудники
│   │   │   └── admin.js             # useAdminStore - статистика
│   │   │
│   │   ├── router/                  # Vue Router
│   │   │   └── index.js             # Конфигурация маршрутов + guards
│   │   │
│   │   ├── styles/                  # CSS стили
│   │   │   ├── main.css             # Главный файл стилей
│   │   │   ├── variables.css        # CSS переменные (цвета, шрифты)
│   │   │   ├── reset.css            # CSS reset
│   │   │   ├── layout.css           # Стили макета (grid, flex)
│   │   │   ├── components.css       # Общие стили компонентов
│   │   │   └── utilities.css        # Утилитарные классы
│   │   │
│   │   ├── utils/                   # Утилиты фронтенда
│   │   │   ├── formatters.js        # Форматирование дат, сумм
│   │   │   ├── validators.js        # Валидация форм
│   │   │   └── constants.js         # Константы
│   │   │
│   │   ├── App.vue                  # Корневой компонент
│   │   └── main.js                  # Точка входа
│   │
│   ├── index.html
│   ├── package.json                 # Зависимости npm
│   ├── vite.config.js               # Конфигурация Vite
│   ├── .env.example                 # Пример переменных окружения
│   ├── Dockerfile                   # Docker для фронтенда
│   └── README.md                    # Документация фронтенда
│
│
├── docker-compose.yml               # Docker Compose для локальной разработки
├── .gitignore                       # Git ignore
└── README.md                        # Главная документация проекта
```

---

## 🗄️ БАЗА ДАННЫХ - 12 ТАБЛИЦ (ПОЛНОЕ ОПИСАНИЕ)

### SQL для создания всех таблиц:

```sql
-- ============================================================================
-- ТАБЛИЦА 1: USER_CLIENTS (Учетные записи клиентов)
-- ============================================================================
CREATE TABLE user_clients (
    id                  SERIAL PRIMARY KEY,
    phone               VARCHAR(20) UNIQUE NOT NULL,
    email               VARCHAR(255) UNIQUE,
    password_hash       VARCHAR(255) NOT NULL,
    is_active           BOOLEAN DEFAULT TRUE,
    is_verified         BOOLEAN DEFAULT FALSE,
    verification_code   VARCHAR(10),
    last_login          TIMESTAMP,
    created_at          TIMESTAMP DEFAULT NOW(),
    updated_at          TIMESTAMP DEFAULT NOW()
);

CREATE UNIQUE INDEX idx_user_phone ON user_clients(phone);
CREATE UNIQUE INDEX idx_user_email ON user_clients(email);


-- ============================================================================
-- ТАБЛИЦА 2: POSITIONS (Должности сотрудников)
-- ============================================================================
CREATE TABLE positions (
    id                  SERIAL PRIMARY KEY,
    name                VARCHAR(255) NOT NULL UNIQUE,
    description         TEXT,
    access_level        INTEGER DEFAULT 1,
    created_at          TIMESTAMP DEFAULT NOW(),
    updated_at          TIMESTAMP DEFAULT NOW()
);

CREATE UNIQUE INDEX idx_position_name ON positions(name);


-- ============================================================================
-- ТАБЛИЦА 3: EMPLOYEES (Сотрудники)
-- ============================================================================
CREATE TABLE employees (
    id                  SERIAL PRIMARY KEY,
    login               VARCHAR(100) UNIQUE NOT NULL,
    password_hash       VARCHAR(255) NOT NULL,
    full_name           VARCHAR(255) NOT NULL,
    position_id         INTEGER NOT NULL,
    phone               VARCHAR(20),
    email               VARCHAR(255) UNIQUE,
    is_active           BOOLEAN DEFAULT TRUE,
    hire_date           DATE,
    last_login          TIMESTAMP,
    created_at          TIMESTAMP DEFAULT NOW(),
    updated_at          TIMESTAMP DEFAULT NOW(),
    
    FOREIGN KEY (position_id) REFERENCES positions(id) ON DELETE RESTRICT
);

CREATE UNIQUE INDEX idx_employee_login ON employees(login);
CREATE UNIQUE INDEX idx_employee_email ON employees(email);
CREATE INDEX idx_employee_position ON employees(position_id);
CREATE INDEX idx_employee_active ON employees(is_active);


-- ============================================================================
-- ТАБЛИЦА 4: COMPANIES (Компании-партнеры)
-- ============================================================================
CREATE TABLE companies (
    id                  SERIAL PRIMARY KEY,
    name                VARCHAR(255) NOT NULL,
    inn                 VARCHAR(12) UNIQUE,
    legal_address       TEXT,
    created_at          TIMESTAMP DEFAULT NOW(),
    updated_at          TIMESTAMP DEFAULT NOW()
);

CREATE UNIQUE INDEX idx_company_inn ON companies(inn);
CREATE INDEX idx_company_name ON companies(name);


-- ============================================================================
-- ТАБЛИЦА 5: CLIENTS (Профили клиентов)
-- ============================================================================
CREATE TABLE clients (
    id                      SERIAL PRIMARY KEY,
    user_id                 INTEGER UNIQUE,
    full_name               VARCHAR(255) NOT NULL,
    date_of_birth           DATE,
    passport_series         VARCHAR(10),
    passport_number         VARCHAR(20),
    passport_issued_by      TEXT,
    passport_issue_date     DATE,
    phone                   VARCHAR(20) NOT NULL,
    email                   VARCHAR(255),
    alternative_phone       VARCHAR(20),
    registration_address    TEXT,
    actual_address          TEXT,
    workplace               VARCHAR(255),
    position                VARCHAR(255),
    monthly_income          DECIMAL(10,2),
    is_verified             BOOLEAN DEFAULT FALSE,
    client_type             VARCHAR(20) DEFAULT 'individual' 
                            CHECK (client_type IN ('individual', 'legal_entity')),
    company_id              INTEGER,
    registration_date       DATE DEFAULT CURRENT_DATE,
    notes                   TEXT,
    created_at              TIMESTAMP DEFAULT NOW(),
    updated_at              TIMESTAMP DEFAULT NOW(),
    
    FOREIGN KEY (user_id) REFERENCES user_clients(id) ON DELETE SET NULL,
    FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE SET NULL
);

CREATE UNIQUE INDEX idx_client_user ON clients(user_id);
CREATE INDEX idx_client_phone ON clients(phone);
CREATE INDEX idx_client_email ON clients(email);
CREATE INDEX idx_client_verified ON clients(is_verified);


-- ============================================================================
-- ТАБЛИЦА 6: PROPERTIES (Объекты недвижимости)
-- ============================================================================
CREATE TABLE properties (
    id                  SERIAL PRIMARY KEY,
    type                VARCHAR(20) NOT NULL 
                        CHECK (type IN ('commercial', 'residential')),
    subtype             VARCHAR(100),
    address             TEXT NOT NULL,
    area                DECIMAL(10,2) NOT NULL,
    rooms_count         INTEGER,
    floor               INTEGER,
    total_floors        INTEGER,
    renovation_type     VARCHAR(100),
    is_furnished        BOOLEAN DEFAULT FALSE,
    monthly_rent        DECIMAL(10,2) NOT NULL,
    utilities_included  BOOLEAN DEFAULT FALSE,
    deposit_amount      DECIMAL(10,2),
    description         TEXT,
    amenities           TEXT,
    photos              TEXT,
    video_url           VARCHAR(500),
    status              VARCHAR(20) DEFAULT 'available' 
                        CHECK (status IN ('available', 'reserved', 'rented', 'maintenance')),
    published_at        TIMESTAMP,
    created_at          TIMESTAMP DEFAULT NOW(),
    updated_at          TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_property_type ON properties(type);
CREATE INDEX idx_property_status ON properties(status);
CREATE INDEX idx_property_rent ON properties(monthly_rent);
CREATE INDEX idx_property_area ON properties(area);


-- ============================================================================
-- ТАБЛИЦА 7: APPLICATIONS (Заявки на аренду)
-- ============================================================================
CREATE TABLE applications (
    id                      SERIAL PRIMARY KEY,
    client_id               INTEGER NOT NULL,
    property_id             INTEGER NOT NULL,
    application_date        DATE DEFAULT CURRENT_DATE,
    status                  VARCHAR(20) DEFAULT 'pending' 
                            CHECK (status IN ('pending', 'under_review', 'approved', 'rejected', 'cancelled')),
    preferred_move_in_date  DATE,
    lease_duration_months   INTEGER,
    notes                   TEXT,
    rejection_reason        TEXT,
    created_at              TIMESTAMP DEFAULT NOW(),
    updated_at              TIMESTAMP DEFAULT NOW(),
    
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
    FOREIGN KEY (property_id) REFERENCES properties(id) ON DELETE CASCADE
);

CREATE INDEX idx_application_client ON applications(client_id);
CREATE INDEX idx_application_property ON applications(property_id);
CREATE INDEX idx_application_status ON applications(status);
CREATE INDEX idx_application_date ON applications(application_date);


-- ============================================================================
-- ТАБЛИЦА 8: TENANT_VERIFICATIONS (Проверка арендаторов)
-- ============================================================================
CREATE TABLE tenant_verifications (
    id                      SERIAL PRIMARY KEY,
    client_id               INTEGER NOT NULL,
    verified_by             INTEGER,
    verification_date       DATE DEFAULT CURRENT_DATE,
    income_verified         BOOLEAN DEFAULT FALSE,
    credit_score            INTEGER,
    employment_verified     BOOLEAN DEFAULT FALSE,
    criminal_record_check   BOOLEAN DEFAULT FALSE,
    previous_rentals_check  BOOLEAN DEFAULT FALSE,
    result                  VARCHAR(30) NOT NULL 
                            CHECK (result IN ('approved', 'conditionally_approved', 'rejected')),
    rejection_reason        TEXT,
    notes                   TEXT,
    documents_checked       TEXT,
    created_at              TIMESTAMP DEFAULT NOW(),
    
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
    FOREIGN KEY (verified_by) REFERENCES employees(id) ON DELETE SET NULL
);

CREATE INDEX idx_verification_client ON tenant_verifications(client_id);
CREATE INDEX idx_verification_result ON tenant_verifications(result);
CREATE INDEX idx_verification_date ON tenant_verifications(verification_date);


-- ============================================================================
-- ТАБЛИЦА 9: CONTRACTS (Договоры аренды)
-- ============================================================================
CREATE TABLE contracts (
    id                      SERIAL PRIMARY KEY,
    contract_number         VARCHAR(50) UNIQUE NOT NULL,
    client_id               INTEGER NOT NULL,
    property_id             INTEGER NOT NULL,
    employee_id             INTEGER,
    signing_date            DATE NOT NULL,
    start_date              DATE NOT NULL,
    end_date                DATE NOT NULL,
    monthly_rent            DECIMAL(10,2) NOT NULL,
    deposit_amount          DECIMAL(10,2),
    deposit_paid            BOOLEAN DEFAULT FALSE,
    contract_status         VARCHAR(20) DEFAULT 'active' 
                            CHECK (contract_status IN ('active', 'expired', 'terminated', 'suspended')),
    payment_day             INTEGER DEFAULT 1,
    payment_method          VARCHAR(50),
    additional_services     TEXT,
    contract_file_url       VARCHAR(500),
    signed_electronically   BOOLEAN DEFAULT FALSE,
    termination_date        DATE,
    termination_reason      TEXT,
    notes                   TEXT,
    created_at              TIMESTAMP DEFAULT NOW(),
    updated_at              TIMESTAMP DEFAULT NOW(),
    
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
    FOREIGN KEY (property_id) REFERENCES properties(id) ON DELETE CASCADE,
    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE SET NULL
);

CREATE UNIQUE INDEX idx_contract_number ON contracts(contract_number);
CREATE INDEX idx_contract_client ON contracts(client_id);
CREATE INDEX idx_contract_property ON contracts(property_id);
CREATE INDEX idx_contract_status ON contracts(contract_status);
CREATE INDEX idx_contract_dates ON contracts(start_date, end_date);


-- ============================================================================
-- ТАБЛИЦА 10: PAYMENTS (Платежи)
-- ============================================================================
CREATE TABLE payments (
    id                  SERIAL PRIMARY KEY,
    contract_id         INTEGER NOT NULL,
    payment_date        DATE NOT NULL,
    amount              DECIMAL(10,2) NOT NULL,
    payment_type        VARCHAR(20) DEFAULT 'rent' 
                        CHECK (payment_type IN ('rent', 'deposit', 'utilities', 'service', 'penalty')),
    payment_method      VARCHAR(50),
    payment_status      VARCHAR(20) DEFAULT 'pending' 
                        CHECK (payment_status IN ('pending', 'completed', 'failed', 'refunded')),
    transaction_id      VARCHAR(100),
    period_month        INTEGER,
    period_year         INTEGER,
    is_late             BOOLEAN DEFAULT FALSE,
    late_days           INTEGER DEFAULT 0,
    penalty_amount      DECIMAL(10,2) DEFAULT 0,
    notes               TEXT,
    created_at          TIMESTAMP DEFAULT NOW(),
    
    FOREIGN KEY (contract_id) REFERENCES contracts(id) ON DELETE CASCADE
);

CREATE INDEX idx_payment_contract ON payments(contract_id);
CREATE INDEX idx_payment_date ON payments(payment_date);
CREATE INDEX idx_payment_status ON payments(payment_status);
CREATE INDEX idx_payment_period ON payments(period_year, period_month);


-- ============================================================================
-- ТАБЛИЦА 11: ADDITIONAL_SERVICES (Дополнительные услуги)
-- ============================================================================
CREATE TABLE additional_services (
    id                  SERIAL PRIMARY KEY,
    name                VARCHAR(255) NOT NULL,
    description         TEXT,
    price               DECIMAL(10,2) NOT NULL,
    unit                VARCHAR(50),
    is_active           BOOLEAN DEFAULT TRUE,
    created_at          TIMESTAMP DEFAULT NOW(),
    updated_at          TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_service_active ON additional_services(is_active);


-- ============================================================================
-- ТАБЛИЦА 12: REVIEWS (Отзывы клиентов)
-- ============================================================================
CREATE TABLE reviews (
    id                  SERIAL PRIMARY KEY,
    client_id           INTEGER NOT NULL,
    property_id         INTEGER,
    rating              INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
    text                TEXT,
    review_date         DATE DEFAULT CURRENT_DATE,
    is_approved         BOOLEAN DEFAULT FALSE,
    created_at          TIMESTAMP DEFAULT NOW(),
    
    FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
    FOREIGN KEY (property_id) REFERENCES properties(id) ON DELETE SET NULL
);

CREATE INDEX idx_review_client ON reviews(client_id);
CREATE INDEX idx_review_property ON reviews(property_id);
CREATE INDEX idx_review_approved ON reviews(is_approved);
```

---

## 🔧 БЭКЕНД - ПОЛНАЯ СПЕЦИФИКАЦИЯ

### 1. requirements.txt

```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
pydantic==2.5.0
pydantic-settings==2.1.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
alembic==1.12.1
python-dotenv==1.0.0
```

### 2. .env.example

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/rentflow_db

# Security
SECRET_KEY=your-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000

# SMS/Email (опционально)
SMS_API_KEY=your-sms-api-key
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-email-password
```

### 3. main.py (Главный файл)

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine, Base
from db import init_data

# Импорт всех роутеров
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

# Создание приложения
app = FastAPI(
    title="RentFlow API",
    description="API для системы управления арендой недвижимости",
    version="1.0.0"
)

# CORS настройки
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Создание таблиц при запуске
@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)
    # Загрузка начальных данных (должности, тестовые пользователи)
    # init_data.load_initial_data()

# Подключение клиентских роутеров
app.include_router(client_auth.router, prefix="/api/client/auth", tags=["Client Auth"])
app.include_router(profile.router, prefix="/api/client/profile", tags=["Client Profile"])
app.include_router(properties.router, prefix="/api/client/properties", tags=["Client Properties"])
app.include_router(applications.router, prefix="/api/client/applications", tags=["Client Applications"])
app.include_router(contracts.router, prefix="/api/client/contracts", tags=["Client Contracts"])
app.include_router(payments.router, prefix="/api/client/payments", tags=["Client Payments"])
app.include_router(reviews.router, prefix="/api/client/reviews", tags=["Client Reviews"])
app.include_router(services.router, prefix="/api/client/services", tags=["Client Services"])

# Подключение роутера сотрудников
app.include_router(employee_auth.router, prefix="/api/employee/auth", tags=["Employee Auth"])

# Подключение админских роутеров
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

# Главная страница
@app.get("/")
def read_root():
    return {
        "message": "Welcome to RentFlow API",
        "docs": "/docs",
        "version": "1.0.0"
    }

# Healthcheck
@app.get("/health")
def health_check():
    return {"status": "healthy"}
```

### 4. db/database.py

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/rentflow_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency для FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### 5. utils/security.py (JWT и хэширование)

```python
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import os

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/client/auth/login")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

# Dependency для получения текущего пользователя
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_token(token)
    if payload is None:
        raise credentials_exception
    
    user_id: str = payload.get("sub")
    user_type: str = payload.get("type")  # "client" или "employee"
    
    if user_id is None:
        raise credentials_exception
    
    # Здесь получаем пользователя из БД в зависимости от типа
    # Возвращаем объект пользователя
    
    return {"id": user_id, "type": user_type}
```

---

## 💻 ФРОНТЕНД - ПОЛНАЯ СПЕЦИФИКАЦИЯ

### 1. package.json

```json
{
  "name": "rentflow-frontend",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "vue": "^3.3.8",
    "vue-router": "^4.2.5",
    "pinia": "^2.1.7",
    "axios": "^1.6.2"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^4.5.0",
    "vite": "^5.0.2"
  }
}
```

### 2. vite.config.js

```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  },
  css: {
    modules: {
      localsConvention: 'camelCase'
    }
  }
})
```

### 3. src/styles/main.css (Главный файл стилей)

```css
/* Импорт всех стилей */
@import './reset.css';
@import './variables.css';
@import './layout.css';
@import './components.css';
@import './utilities.css';

/* Глобальные стили */
* {
  box-sizing: border-box;
}

body {
  font-family: var(--font-family);
  font-size: var(--font-size-base);
  line-height: 1.6;
  color: var(--text-color);
  background-color: var(--bg-color);
}

a {
  text-decoration: none;
  color: var(--primary-color);
}

a:hover {
  color: var(--primary-dark);
}

img {
  max-width: 100%;
  height: auto;
}
```

### 4. src/styles/variables.css (CSS переменные)

```css
:root {
  /* Цвета */
  --primary-color: #2563eb;
  --primary-dark: #1d4ed8;
  --primary-light: #3b82f6;
  
  --secondary-color: #10b981;
  --secondary-dark: #059669;
  --secondary-light: #34d399;
  
  --danger-color: #ef4444;
  --danger-dark: #dc2626;
  --danger-light: #f87171;
  
  --warning-color: #f59e0b;
  --success-color: #10b981;
  
  --text-color: #1f2937;
  --text-light: #6b7280;
  --text-dark: #111827;
  
  --bg-color: #ffffff;
  --bg-gray: #f9fafb;
  --bg-dark: #111827;
  
  --border-color: #e5e7eb;
  --border-dark: #d1d5db;
  
  /* Шрифты */
  --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --font-size-3xl: 1.875rem;
  --font-size-4xl: 2.25rem;
  
  /* Отступы */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;
  --spacing-2xl: 3rem;
  
  /* Радиусы */
  --radius-sm: 0.25rem;
  --radius-md: 0.375rem;
  --radius-lg: 0.5rem;
  --radius-xl: 0.75rem;
  --radius-full: 9999px;
  
  /* Тени */
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
  
  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-base: 200ms ease;
  --transition-slow: 300ms ease;
  
  /* Z-indexes */
  --z-dropdown: 1000;
  --z-sticky: 1020;
  --z-fixed: 1030;
  --z-modal-backdrop: 1040;
  --z-modal: 1050;
  --z-popover: 1060;
  --z-tooltip: 1070;
}
```

### 5. src/styles/components.css (Стили компонентов)

```css
/* Кнопки */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-sm) var(--spacing-lg);
  font-size: var(--font-size-base);
  font-weight: 500;
  line-height: 1.5;
  border-radius: var(--radius-md);
  border: 1px solid transparent;
  cursor: pointer;
  transition: all var(--transition-base);
  text-decoration: none;
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.btn-primary {
  background-color: var(--primary-color);
  color: white;
  border-color: var(--primary-color);
}

.btn-primary:hover:not(:disabled) {
  background-color: var(--primary-dark);
  border-color: var(--primary-dark);
}

.btn-secondary {
  background-color: var(--secondary-color);
  color: white;
  border-color: var(--secondary-color);
}

.btn-secondary:hover:not(:disabled) {
  background-color: var(--secondary-dark);
  border-color: var(--secondary-dark);
}

.btn-danger {
  background-color: var(--danger-color);
  color: white;
  border-color: var(--danger-color);
}

.btn-danger:hover:not(:disabled) {
  background-color: var(--danger-dark);
  border-color: var(--danger-dark);
}

.btn-outline {
  background-color: transparent;
  color: var(--primary-color);
  border-color: var(--primary-color);
}

.btn-outline:hover:not(:disabled) {
  background-color: var(--primary-color);
  color: white;
}

/* Инпуты */
.input {
  width: 100%;
  padding: var(--spacing-sm) var(--spacing-md);
  font-size: var(--font-size-base);
  line-height: 1.5;
  color: var(--text-color);
  background-color: white;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  transition: border-color var(--transition-base);
}

.input:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.input:disabled {
  background-color: var(--bg-gray);
  cursor: not-allowed;
}

.input-error {
  border-color: var(--danger-color);
}

.input-error:focus {
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.1);
}

/* Карточки */
.card {
  background-color: white;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  padding: var(--spacing-lg);
  transition: box-shadow var(--transition-base);
}

.card:hover {
  box-shadow: var(--shadow-lg);
}

.card-header {
  margin-bottom: var(--spacing-md);
  padding-bottom: var(--spacing-md);
  border-bottom: 1px solid var(--border-color);
}

.card-title {
  font-size: var(--font-size-xl);
  font-weight: 600;
  color: var(--text-dark);
  margin: 0;
}

.card-body {
  margin-bottom: var(--spacing-md);
}

.card-footer {
  margin-top: var(--spacing-md);
  padding-top: var(--spacing-md);
  border-top: 1px solid var(--border-color);
}

/* Модальные окна */
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: var(--z-modal-backdrop);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal {
  background-color: white;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-xl);
  max-width: 500px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
  z-index: var(--z-modal);
}

.modal-header {
  padding: var(--spacing-lg);
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-title {
  font-size: var(--font-size-xl);
  font-weight: 600;
  margin: 0;
}

.modal-close {
  background: none;
  border: none;
  font-size: var(--font-size-2xl);
  cursor: pointer;
  color: var(--text-light);
  padding: 0;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-md);
  transition: background-color var(--transition-base);
}

.modal-close:hover {
  background-color: var(--bg-gray);
}

.modal-body {
  padding: var(--spacing-lg);
}

.modal-footer {
  padding: var(--spacing-lg);
  border-top: 1px solid var(--border-color);
  display: flex;
  justify-content: flex-end;
  gap: var(--spacing-sm);
}

/* Таблицы */
.table {
  width: 100%;
  border-collapse: collapse;
}

.table th,
.table td {
  padding: var(--spacing-md);
  text-align: left;
  border-bottom: 1px solid var(--border-color);
}

.table th {
  font-weight: 600;
  color: var(--text-dark);
  background-color: var(--bg-gray);
}

.table tbody tr:hover {
  background-color: var(--bg-gray);
}

/* Бейджи */
.badge {
  display: inline-flex;
  align-items: center;
  padding: var(--spacing-xs) var(--spacing-sm);
  font-size: var(--font-size-sm);
  font-weight: 500;
  border-radius: var(--radius-full);
}

.badge-primary {
  background-color: rgba(37, 99, 235, 0.1);
  color: var(--primary-color);
}

.badge-success {
  background-color: rgba(16, 185, 129, 0.1);
  color: var(--success-color);
}

.badge-danger {
  background-color: rgba(239, 68, 68, 0.1);
  color: var(--danger-color);
}

.badge-warning {
  background-color: rgba(245, 158, 11, 0.1);
  color: var(--warning-color);
}

/* Лоадер */
.loader {
  border: 3px solid var(--bg-gray);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Пагинация */
.pagination {
  display: flex;
  gap: var(--spacing-xs);
  list-style: none;
  padding: 0;
  margin: 0;
}

.pagination-item {
  display: flex;
}

.pagination-link {
  padding: var(--spacing-sm) var(--spacing-md);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  color: var(--text-color);
  cursor: pointer;
  transition: all var(--transition-base);
}

.pagination-link:hover {
  background-color: var(--bg-gray);
  border-color: var(--border-dark);
}

.pagination-link.active {
  background-color: var(--primary-color);
  color: white;
  border-color: var(--primary-color);
}

.pagination-link:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
```

### 6. src/router/index.js (Полная маршрутизация)

```javascript
import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const routes = [
  // Публичные маршруты
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/client/HomePage.vue')
  },
  {
    path: '/properties',
    name: 'Properties',
    component: () => import('@/views/client/PropertiesPage.vue')
  },
  {
    path: '/properties/:id',
    name: 'PropertyDetail',
    component: () => import('@/views/client/PropertyDetailPage.vue')
  },
  
  // Авторизация клиентов
  {
    path: '/client/login',
    name: 'ClientLogin',
    component: () => import('@/views/auth/ClientLoginPage.vue')
  },
  {
    path: '/client/register',
    name: 'ClientRegister',
    component: () => import('@/views/auth/ClientRegisterPage.vue')
  },
  {
    path: '/client/verify-phone',
    name: 'VerifyPhone',
    component: () => import('@/views/auth/VerifyPhonePage.vue'),
    meta: { requiresAuth: true, role: 'client' }
  },
  
  // Защищенные клиентские маршруты
  {
    path: '/client/profile',
    name: 'ClientProfile',
    component: () => import('@/views/client/ProfilePage.vue'),
    meta: { requiresAuth: true, role: 'client' }
  },
  {
    path: '/client/applications',
    name: 'ClientApplications',
    component: () => import('@/views/client/ApplicationsPage.vue'),
    meta: { requiresAuth: true, role: 'client' }
  },
  {
    path: '/client/contracts',
    name: 'ClientContracts',
    component: () => import('@/views/client/ContractsPage.vue'),
    meta: { requiresAuth: true, role: 'client' }
  },
  {
    path: '/client/payments',
    name: 'ClientPayments',
    component: () => import('@/views/client/PaymentsPage.vue'),
    meta: { requiresAuth: true, role: 'client' }
  },
  {
    path: '/client/reviews',
    name: 'ClientReviews',
    component: () => import('@/views/client/ReviewsPage.vue'),
    meta: { requiresAuth: true, role: 'client' }
  },
  
  // Вход сотрудников
  {
    path: '/employee/login',
    name: 'EmployeeLogin',
    component: () => import('@/views/auth/EmployeeLoginPage.vue')
  },
  
  // Админские маршруты
  {
    path: '/admin',
    redirect: '/admin/dashboard'
  },
  {
    path: '/admin/dashboard',
    name: 'AdminDashboard',
    component: () => import('@/views/admin/DashboardPage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/properties',
    name: 'AdminProperties',
    component: () => import('@/views/admin/PropertiesManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/applications',
    name: 'AdminApplications',
    component: () => import('@/views/admin/ApplicationsManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/clients',
    name: 'AdminClients',
    component: () => import('@/views/admin/ClientsManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/verifications',
    name: 'AdminVerifications',
    component: () => import('@/views/admin/VerificationsManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/contracts',
    name: 'AdminContracts',
    component: () => import('@/views/admin/ContractsManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/payments',
    name: 'AdminPayments',
    component: () => import('@/views/admin/PaymentsManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/employees',
    name: 'AdminEmployees',
    component: () => import('@/views/admin/EmployeesManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/positions',
    name: 'AdminPositions',
    component: () => import('@/views/admin/PositionsManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/companies',
    name: 'AdminCompanies',
    component: () => import('@/views/admin/CompaniesManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/services',
    name: 'AdminServices',
    component: () => import('@/views/admin/ServicesManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/reviews',
    name: 'AdminReviews',
    component: () => import('@/views/admin/ReviewsManagePage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  },
  {
    path: '/admin/statistics',
    name: 'AdminStatistics',
    component: () => import('@/views/admin/StatisticsPage.vue'),
    meta: { requiresAuth: true, role: 'employee' }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Navigation Guards
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  
  if (to.meta.requiresAuth) {
    if (!authStore.isAuthenticated) {
      // Не авторизован - редирект на логин
      if (to.meta.role === 'client') {
        next('/client/login')
      } else {
        next('/employee/login')
      }
    } else if (to.meta.role && authStore.userRole !== to.meta.role) {
      // Авторизован, но не та роль
      next('/')
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
```

---

## 📅 ПОШАГОВЫЙ РОАДМАП РАЗРАБОТКИ

### ФАЗА 1: Подготовка (День 1)
```
□ Создать репозиторий GitHub: RentFlow
□ Создать структуру папок backend/ и frontend/
□ Настроить .gitignore
□ Создать README.md
```

### ФАЗА 2: Backend - База данных (День 2-4)
```
□ Установить PostgreSQL локально
□ Создать БД: rentflow_db
□ Выполнить SQL скрипт создания всех 12 таблиц
□ Создать backend/db/database.py
□ Создать backend/db/models.py (12 моделей SQLAlchemy)
□ Создать backend/db/init_data.py (начальные данные)
□ Создать backend/requirements.txt
□ Установить зависимости: pip install -r requirements.txt
```

### ФАЗА 3: Backend - Pydantic схемы (День 5-6)
```
□ Создать backend/schemas/user.py
□ Создать backend/schemas/client.py
□ Создать backend/schemas/property.py
□ Создать backend/schemas/application.py
□ Создать backend/schemas/contract.py
□ Создать backend/schemas/payment.py
□ Создать backend/schemas/verification.py
□ Создать backend/schemas/employee.py
□ Создать backend/schemas/position.py
□ Создать backend/schemas/company.py
□ Создать backend/schemas/service.py
□ Создать backend/schemas/review.py
```

### ФАЗА 4: Backend - Utils (День 7)
```
□ Создать backend/utils/security.py (JWT, хэширование)
□ Создать backend/utils/validators.py
□ Создать backend/utils/notifications.py
□ Создать backend/utils/file_upload.py
```

### ФАЗА 5: Backend - Клиентские API (День 8-12)
```
□ Создать backend/routers/client/auth.py
□ Создать backend/routers/client/profile.py
□ Создать backend/routers/client/properties.py
□ Создать backend/routers/client/applications.py
□ Создать backend/routers/client/contracts.py
□ Создать backend/routers/client/payments.py
□ Создать backend/routers/client/reviews.py
□ Создать backend/routers/client/services.py
□ Создать backend/main.py
□ Тестировать все эндпоинты в Swagger
```

### ФАЗА 6: Backend - Админские API (День 13-20)
```
□ Создать backend/routers/employee/auth.py
□ Создать backend/routers/admin/properties.py
□ Создать backend/routers/admin/applications.py
□ Создать backend/routers/admin/clients.py
□ Создать backend/routers/admin/verifications.py
□ Создать backend/routers/admin/contracts.py
□ Создать backend/routers/admin/payments.py
□ Создать backend/routers/admin/employees.py
□ Создать backend/routers/admin/positions.py
□ Создать backend/routers/admin/companies.py
□ Создать backend/routers/admin/services.py
□ Создать backend/routers/admin/reviews.py
□ Создать backend/routers/admin/statistics.py
□ Тестировать все админские эндпоинты
```

### ФАЗА 7: Frontend - Настройка (День 21-22)
```
□ Создать Vue 3 проект: npm create vite@latest frontend -- --template vue
□ Установить зависимости: vue-router, pinia, axios
□ Создать структуру папок (как в спецификации выше)
□ Создать vite.config.js
□ Создать все CSS файлы (variables, reset, layout, components, utilities)
□ Создать frontend/src/router/index.js
□ Создать frontend/src/api/axios.js
```

### ФАЗА 8: Frontend - API Services и Stores (День 23-24)
```
□ Создать frontend/src/api/services/auth.js
□ Создать frontend/src/api/services/properties.js
□ Создать frontend/src/api/services/applications.js
□ Создать frontend/src/api/services/contracts.js
□ Создать frontend/src/api/services/payments.js
□ Создать frontend/src/api/services/clients.js
□ Создать frontend/src/api/services/employees.js
□ Создать frontend/src/api/services/admin.js
□ Создать frontend/src/stores/auth.js
□ Создать frontend/src/stores/properties.js
□ Создать frontend/src/stores/applications.js
□ Создать frontend/src/stores/contracts.js
□ Создать frontend/src/stores/payments.js
□ Создать frontend/src/stores/clients.js
□ Создать frontend/src/stores/employees.js
□ Создать frontend/src/stores/admin.js
```

### ФАЗА 9: Frontend - Общие компоненты (День 25)
```
□ Создать frontend/src/components/common/BaseButton.vue
□ Создать frontend/src/components/common/BaseInput.vue
□ Создать frontend/src/components/common/BaseCard.vue
□ Создать frontend/src/components/common/BaseModal.vue
□ Создать frontend/src/components/common/BaseLoader.vue
□ Создать frontend/src/components/common/BasePagination.vue
□ Создать frontend/src/components/common/BaseTable.vue
```

### ФАЗА 10: Frontend - Layout компоненты (День 26)
```
□ Создать frontend/src/components/layout/AppHeader.vue
□ Создать frontend/src/components/layout/AppFooter.vue
□ Создать frontend/src/components/layout/ClientSidebar.vue
□ Создать frontend/src/components/layout/AdminSidebar.vue
```

### ФАЗА 11: Frontend - Страницы авторизации (День 27)
```
□ Создать frontend/src/views/auth/ClientLoginPage.vue
□ Создать frontend/src/views/auth/ClientRegisterPage.vue
□ Создать frontend/src/views/auth/EmployeeLoginPage.vue
□ Создать frontend/src/views/auth/VerifyPhonePage.vue
```

### ФАЗА 12: Frontend - Клиентские страницы (День 28-33)
```
□ Создать frontend/src/views/client/HomePage.vue
□ Создать frontend/src/components/property/PropertyCard.vue
□ Создать frontend/src/components/property/PropertyFilter.vue
□ Создать frontend/src/views/client/PropertiesPage.vue
□ Создать frontend/src/components/property/PropertyGallery.vue
□ Создать frontend/src/views/client/PropertyDetailPage.vue
□ Создать frontend/src/views/client/ProfilePage.vue
□ Создать frontend/src/components/application/ApplicationForm.vue
□ Создать frontend/src/components/application/ApplicationCard.vue
□ Создать frontend/src/views/client/ApplicationsPage.vue
□ Создать frontend/src/components/contract/ContractCard.vue
□ Создать frontend/src/views/client/ContractsPage.vue
□ Создать frontend/src/views/client/PaymentsPage.vue
□ Создать frontend/src/views/client/ReviewsPage.vue
```

### ФАЗА 13: Frontend - Админские страницы (День 34-45)
```
□ Создать frontend/src/components/admin/StatCard.vue
□ Создать frontend/src/views/admin/DashboardPage.vue
□ Создать frontend/src/components/admin/DataTable.vue
□ Создать frontend/src/components/property/PropertyForm.vue
□ Создать frontend/src/views/admin/PropertiesManagePage.vue
□ Создать frontend/src/views/admin/ApplicationsManagePage.vue
□ Создать frontend/src/views/admin/ClientsManagePage.vue
□ Создать frontend/src/views/admin/VerificationsManagePage.vue
□ Создать frontend/src/components/contract/ContractForm.vue
□ Создать frontend/src/views/admin/ContractsManagePage.vue
□ Создать frontend/src/views/admin/PaymentsManagePage.vue
□ Создать frontend/src/views/admin/EmployeesManagePage.vue
□ Создать frontend/src/views/admin/PositionsManagePage.vue
□ Создать frontend/src/views/admin/CompaniesManagePage.vue
□ Создать frontend/src/views/admin/ServicesManagePage.vue
□ Создать frontend/src/views/admin/ReviewsManagePage.vue
□ Создать frontend/src/views/admin/StatisticsPage.vue
```

### ФАЗА 14: Тестирование (День 46-48)
```
□ End-to-End тестирование всего цикла
□ Проверить регистрацию → заявку → договор
□ Проверить все формы на валидацию
□ Проверить авторизацию и защищенные маршруты
□ Проверить админку
□ Проверить адаптивность
□ Исправить найденные баги
```

### ФАЗА 15: Документация (День 49-50)
```
□ Написать backend/README.md
□ Написать frontend/README.md
□ Написать главный README.md
□ Задокументировать API в Swagger
```

### ФАЗА 16: Деплой (День 51-55)
```
□ Создать PostgreSQL на Render
□ Задеплоить бэкенд на Render
□ Применить миграции
□ Загрузить начальные данные
□ Задеплоить фронтенд на Netlify
□ Настроить переменные окружения
□ Проверить работу в продакшене
```

---

## ✅ ЧЕКЛИСТ ДЛЯ CLAUDE CODE

Когда будешь реализовывать этот проект в Claude Code, следуй этому порядку:

### ДЕНЬ 1-4: База данных
- [ ] Создай все 12 таблиц SQL
- [ ] Создай models.py с SQLAlchemy моделями
- [ ] Создай database.py
- [ ] Создай init_data.py

### ДЕНЬ 5-7: Pydantic схемы и Utils
- [ ] Создай все 12 Pydantic схем
- [ ] Создай security.py (JWT, хэширование)
- [ ] Создай validators.py

### ДЕНЬ 8-20: Все API эндпоинты
- [ ] Создай main.py
- [ ] Создай 8 клиентских роутеров
- [ ] Создай 13 админских роутеров
- [ ] Протестируй все через Swagger

### ДЕНЬ 21-26: Frontend базис
- [ ] Настрой Vite проект
- [ ] Создай все CSS файлы
- [ ] Создай router с маршрутами
- [ ] Создай 8 API services
- [ ] Создай 8 Pinia stores
- [ ] Создай 7 общих компонентов
- [ ] Создай 4 layout компонента

### ДЕНЬ 27-45: Все страницы
- [ ] Создай 4 страницы авторизации
- [ ] Создай 8 клиентских страниц
- [ ] Создай 14 админских страниц
- [ ] Создай все специфичные компоненты

### ДЕНЬ 46-55: Финал
- [ ] Протестируй весь функционал
- [ ] Напиши документацию
- [ ] Задеплой на Render + Netlify

---

## 🎉 РЕЗУЛЬТАТ

После реализации всех этапов получится:
- ✅ Полнофункциональная система управления арендой
- ✅ 12 таблиц БД с данными
- ✅ 50+ работающих API эндпоинтов
- ✅ 40+ страниц на Vue.js с чистым CSS
- ✅ Личный кабинет клиента
- ✅ Админ-панель для сотрудников
- ✅ Онлайн-бронирование и оплата
- ✅ Система проверки арендаторов

**Название:** RentFlow  
**Стек:** FastAPI + Vue.js 3 + PostgreSQL + Pure CSS  
**Готово к реализации в Claude Code!** 🚀

