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

# Создание FastAPI приложения
app = FastAPI(
    title="RentFlow API",
    description="API для системы управления арендой недвижимости",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware - Разрешить все источники для разработки
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все источники
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Создание таблиц и начальных данных при запуске
@app.on_event("startup")
async def startup_event():
    print("🚀 Запуск RentFlow API...")
    Base.metadata.create_all(bind=engine)
    print("✅ Таблицы базы данных созданы")

    # Создание начальных данных
    db = next(get_db())
    try:
        create_initial_data(db)
    except Exception as e:
        print(f"Создание начальных данных: {e}")
    finally:
        db.close()

# Роутеры клиента
app.include_router(client_auth.router, prefix="/api/client/auth", tags=["Авторизация клиента"])
app.include_router(profile.router, prefix="/api/client/profile", tags=["Профиль клиента"])
app.include_router(properties.router, prefix="/api/client/properties", tags=["Объекты клиента"])
app.include_router(applications.router, prefix="/api/client/applications", tags=["Заявки клиента"])
app.include_router(contracts.router, prefix="/api/client/contracts", tags=["Контракты клиента"])
app.include_router(payments.router, prefix="/api/client/payments", tags=["Платежи клиента"])
app.include_router(reviews.router, prefix="/api/client/reviews", tags=["Отзывы клиента"])
app.include_router(services.router, prefix="/api/client/services", tags=["Услуги клиента"])

# Роутер сотрудника
app.include_router(employee_auth.router, prefix="/api/employee/auth", tags=["Авторизация сотрудника"])

# Роутеры администратора
app.include_router(admin_properties.router, prefix="/api/admin/properties", tags=["Админ: Объекты"])
app.include_router(admin_applications.router, prefix="/api/admin/applications", tags=["Админ: Заявки"])
app.include_router(admin_clients.router, prefix="/api/admin/clients", tags=["Админ: Клиенты"])
app.include_router(verifications.router, prefix="/api/admin/verifications", tags=["Админ: Верификации"])
app.include_router(admin_contracts.router, prefix="/api/admin/contracts", tags=["Админ: Контракты"])
app.include_router(admin_payments.router, prefix="/api/admin/payments", tags=["Админ: Платежи"])
app.include_router(admin_employees.router, prefix="/api/admin/employees", tags=["Админ: Сотрудники"])
app.include_router(positions.router, prefix="/api/admin/positions", tags=["Админ: Должности"])
app.include_router(companies.router, prefix="/api/admin/companies", tags=["Админ: Компании"])
app.include_router(admin_services.router, prefix="/api/admin/services", tags=["Админ: Услуги"])
app.include_router(admin_reviews.router, prefix="/api/admin/reviews", tags=["Админ: Отзывы"])
app.include_router(statistics.router, prefix="/api/admin/statistics", tags=["Админ: Статистика"])

# Корневой эндпоинт
@app.get("/")
def read_root():
    return {
        "message": "Добро пожаловать в RentFlow API",
        "version": "2.0.0",
        "status": "operational",
        "docs": "/docs",
        "redoc": "/redoc",
        "features": [
            "50+ API эндпоинтов",
            "12 таблиц базы данных",
            "Полный CRUD функционал",
            "Тестовые данные включены"
        ]
    }

# Эндпоинты проверки здоровья для мониторинга
@app.get("/health")
@app.head("/health")
def health_check():
    return {"status": "healthy", "service": "RentFlow API v2.0"}
