from sqlalchemy.orm import Session
from db.models import (
    Position, Employee, Company, Property, Client, UserClient,
    Application, Contract, Payment, AdditionalService, Review
)
from datetime import date, datetime, timedelta
from decimal import Decimal


def create_initial_data(db: Session):
    """Create initial test data for the database"""

    # Check if data already exists
    if db.query(Position).first():
        print("Initial data already exists, skipping...")
        return

    print("Creating initial data...")

    # 1. Create Positions
    positions = [
        Position(name="Administrator", description="System administrator", access_level=10),
        Position(name="Manager", description="Property manager", access_level=5),
        Position(name="Agent", description="Rental agent", access_level=3),
    ]
    db.add_all(positions)
    db.commit()
    print("✓ Positions created")

    # 2. Create Employees (plain passwords for educational purposes)
    employees = [
        Employee(
            login="admin",
            password_hash="admin123",  # Plain text password
            full_name="Admin User",
            position_id=1,
            phone="+79991111111",
            email="admin@rentflow.com",
            is_active=True,
            hire_date=date(2024, 1, 1)
        ),
        Employee(
            login="manager1",
            password_hash="manager123",  # Plain text password
            full_name="Ivan Petrov",
            position_id=2,
            phone="+79992222222",
            email="manager@rentflow.com",
            is_active=True,
            hire_date=date(2024, 2, 1)
        ),
    ]
    db.add_all(employees)
    db.commit()
    print("✓ Employees created")

    # 3. Create Companies
    companies = [
        Company(
            name='ООО "Самолет Плюс"',
            inn="7712345678",
            legal_address="Moscow, Red Square, 1"
        ),
        Company(
            name='ООО "Недвижимость XXI"',
            inn="7723456789",
            legal_address="Moscow, Tverskaya, 10"
        ),
    ]
    db.add_all(companies)
    db.commit()
    print("✓ Companies created")

    # 4. Create Properties
    properties = [
        # Residential properties
        Property(
            type="residential",
            subtype="Квартира",
            address="Moscow, Arbat Street, 15, apt 42",
            area=Decimal("75.5"),
            rooms_count=2,
            floor=5,
            total_floors=12,
            renovation_type="Modern",
            is_furnished=True,
            monthly_rent=Decimal("80000"),
            utilities_included=False,
            deposit_amount=Decimal("80000"),
            description="Cozy 2-room apartment in the city center with modern renovation",
            amenities="Wi-Fi, Air conditioning, Washing machine, Dishwasher",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Пентхаус",
            address="Moscow, Leninsky Prospekt, 45, apt 120",
            area=Decimal("120.0"),
            rooms_count=3,
            floor=10,
            total_floors=16,
            renovation_type="Premium",
            is_furnished=True,
            monthly_rent=Decimal("150000"),
            utilities_included=False,
            deposit_amount=Decimal("150000"),
            description="Luxury 3-room apartment with panoramic views",
            amenities="Wi-Fi, Air conditioning, Smart home, Parking",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Студия",
            address="Moscow, Baumanskaya Street, 23, apt 5",
            area=Decimal("35.0"),
            rooms_count=1,
            floor=3,
            total_floors=9,
            renovation_type="Standard",
            is_furnished=True,
            monthly_rent=Decimal("45000"),
            utilities_included=False,
            deposit_amount=Decimal("45000"),
            description="Compact studio near metro station",
            amenities="Wi-Fi, Kitchen appliances",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Таунхаус",
            address="Moscow, Kutuzovsky Prospekt, 12, apt 78",
            area=Decimal("95.0"),
            rooms_count=2,
            floor=15,
            total_floors=25,
            renovation_type="Modern",
            is_furnished=False,
            monthly_rent=Decimal("100000"),
            utilities_included=False,
            deposit_amount=Decimal("100000"),
            description="Spacious apartment in prestigious area",
            amenities="Concierge, Gym, Underground parking",
            status="available",
            published_at=datetime.now()
        ),
        # Commercial properties
        Property(
            type="commercial",
            subtype="Офис",
            address="Moscow, Business Center Tower, 5th floor",
            area=Decimal("200.0"),
            floor=5,
            total_floors=20,
            renovation_type="Business class",
            is_furnished=True,
            monthly_rent=Decimal("300000"),
            utilities_included=True,
            deposit_amount=Decimal("600000"),
            description="Modern office space in business district",
            amenities="Reception, Meeting rooms, Parking, Security",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="commercial",
            subtype="Торговое помещение",
            address="Moscow, Shopping Center Mega, Ground floor",
            area=Decimal("80.0"),
            floor=1,
            total_floors=3,
            renovation_type="Commercial",
            is_furnished=False,
            monthly_rent=Decimal("250000"),
            utilities_included=False,
            deposit_amount=Decimal("500000"),
            description="Retail space in popular shopping center",
            amenities="High foot traffic, Loading bay",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Квартира",
            address="Moscow, Prospekt Mira, 88, apt 202",
            area=Decimal("60.0"),
            rooms_count=2,
            floor=8,
            total_floors=14,
            renovation_type="Standard",
            is_furnished=True,
            monthly_rent=Decimal("65000"),
            utilities_included=False,
            deposit_amount=Decimal("65000"),
            description="Comfortable apartment near VDNKh",
            amenities="Balcony, Internet, Cable TV",
            status="rented",
            published_at=datetime.now() - timedelta(days=30)
        ),
        Property(
            type="residential",
            subtype="Коттедж",
            address="Moscow, Moskva City, Tower Federation, apt 501",
            area=Decimal("250.0"),
            rooms_count=4,
            floor=50,
            total_floors=50,
            renovation_type="Luxury",
            is_furnished=True,
            monthly_rent=Decimal("500000"),
            utilities_included=True,
            deposit_amount=Decimal("1000000"),
            description="Exclusive penthouse with breathtaking views",
            amenities="Private elevator, Terrace, Smart home, Concierge, Spa",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Квартира",
            address="Москва, Тверская ул., 28, кв. 15",
            area=Decimal("52.0"),
            rooms_count=1,
            floor=4,
            total_floors=10,
            renovation_type="Косметический",
            is_furnished=True,
            monthly_rent=Decimal("55000"),
            utilities_included=False,
            deposit_amount=Decimal("55000"),
            description="Однокомнатная квартира в центре Москвы, рядом с метро Тверская",
            amenities="Wi-Fi, Стиральная машина, Балкон",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Студия",
            address="Москва, Ленинский проспект, 92, кв. 8",
            area=Decimal("28.0"),
            rooms_count=1,
            floor=2,
            total_floors=7,
            renovation_type="Евро",
            is_furnished=True,
            monthly_rent=Decimal("38000"),
            utilities_included=False,
            deposit_amount=Decimal("38000"),
            description="Уютная студия для молодой пары или студента",
            amenities="Wi-Fi, Кухонная техника, Холодильник",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Квартира",
            address="Москва, Ломоносовский проспект, 14, кв. 105",
            area=Decimal("85.0"),
            rooms_count=3,
            floor=7,
            total_floors=17,
            renovation_type="Дизайнерский",
            is_furnished=True,
            monthly_rent=Decimal("120000"),
            utilities_included=False,
            deposit_amount=Decimal("120000"),
            description="Трёхкомнатная квартира с дизайнерским ремонтом в престижном районе",
            amenities="Wi-Fi, Посудомоечная машина, Кондиционер, Умный дом, Паркинг",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Пентхаус",
            address="Москва, Новый Арбат, 36, кв. 250",
            area=Decimal("180.0"),
            rooms_count=4,
            floor=20,
            total_floors=20,
            renovation_type="Люкс",
            is_furnished=True,
            monthly_rent=Decimal("350000"),
            utilities_included=True,
            deposit_amount=Decimal("700000"),
            description="Роскошный пентхаус с панорамным видом на Москва-Сити",
            amenities="Панорамные окна, Терраса, Джакузи, Сауна, Умный дом, Консьерж",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="commercial",
            subtype="Офис",
            address="Москва, БЦ Садовая Галерея, 5 этаж",
            area=Decimal("120.0"),
            floor=5,
            total_floors=15,
            renovation_type="Бизнес-класс",
            is_furnished=True,
            monthly_rent=Decimal("180000"),
            utilities_included=True,
            deposit_amount=Decimal("360000"),
            description="Офис в престижном бизнес-центре с отличной транспортной доступностью",
            amenities="Ресепшн, Переговорные, Кухня, Охрана, Паркинг",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Таунхаус",
            address="Москва, Рублево-Успенское шоссе, КП Изумрудные холмы, 15",
            area=Decimal("220.0"),
            rooms_count=5,
            floor=1,
            total_floors=2,
            renovation_type="Премиум",
            is_furnished=True,
            monthly_rent=Decimal("280000"),
            utilities_included=False,
            deposit_amount=Decimal("560000"),
            description="Таунхаус в элитном поселке с развитой инфраструктурой",
            amenities="Гараж, Придомовая территория, Охрана, Детская площадка",
            status="available",
            published_at=datetime.now()
        ),
        # Дополнительные объекты
        Property(
            type="residential",
            subtype="Студия",
            address="Москва, ул. Покровка, 4, кв. 17",
            area=Decimal("32.0"),
            rooms_count=1,
            floor=6,
            total_floors=10,
            renovation_type="Современный",
            is_furnished=True,
            monthly_rent=Decimal("42000"),
            utilities_included=False,
            deposit_amount=Decimal("42000"),
            description="Светлая студия в историческом центре Москвы",
            amenities="Wi-Fi, Кондиционер, Балкон, Встроенная кухня",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Квартира",
            address="Москва, Проспект Вернадского, 78, кв. 245",
            area=Decimal("68.0"),
            rooms_count=2,
            floor=12,
            total_floors=22,
            renovation_type="Современный",
            is_furnished=True,
            monthly_rent=Decimal("75000"),
            utilities_included=False,
            deposit_amount=Decimal("75000"),
            description="Двухкомнатная квартира рядом с МГУ и метро",
            amenities="Wi-Fi, Стиральная машина, Посудомойка, Паркинг",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Квартира",
            address="Москва, Кутузовский проспект, 24, кв. 89",
            area=Decimal("105.0"),
            rooms_count=3,
            floor=18,
            total_floors=30,
            renovation_type="Премиум",
            is_furnished=True,
            monthly_rent=Decimal("160000"),
            utilities_included=True,
            deposit_amount=Decimal("320000"),
            description="Панорамная трёхкомнатная квартира с видом на Москва-Сити",
            amenities="Умный дом, Джакузи, Панорамные окна, Консьерж, Паркинг",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="commercial",
            subtype="Торговое помещение",
            address="Москва, ТЦ Европейский, 2 этаж",
            area=Decimal("65.0"),
            floor=2,
            total_floors=5,
            renovation_type="Коммерческий",
            is_furnished=False,
            monthly_rent=Decimal("220000"),
            utilities_included=False,
            deposit_amount=Decimal("440000"),
            description="Торговая площадь в центральном ТЦ с высокой проходимостью",
            amenities="Витрина, Погрузочная зона, Вентиляция",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Студия",
            address="Москва, Варшавское шоссе, 141, кв. 523",
            area=Decimal("26.0"),
            rooms_count=1,
            floor=14,
            total_floors=25,
            renovation_type="Евро",
            is_furnished=True,
            monthly_rent=Decimal("35000"),
            utilities_included=False,
            deposit_amount=Decimal("35000"),
            description="Компактная студия в новом жилом комплексе",
            amenities="Wi-Fi, Охрана, Детская площадка",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Квартира",
            address="Москва, Зеленоград, корпус 1511, кв. 78",
            area=Decimal("58.0"),
            rooms_count=2,
            floor=9,
            total_floors=16,
            renovation_type="Стандарт",
            is_furnished=True,
            monthly_rent=Decimal("50000"),
            utilities_included=False,
            deposit_amount=Decimal("50000"),
            description="Просторная двушка в спальном районе Зеленограда",
            amenities="Балкон, Интернет, Рядом школа и детский сад",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="commercial",
            subtype="Офис",
            address="Москва, БЦ Белая Площадь, 10 этаж",
            area=Decimal("85.0"),
            floor=10,
            total_floors=18,
            renovation_type="Бизнес-класс",
            is_furnished=True,
            monthly_rent=Decimal("140000"),
            utilities_included=True,
            deposit_amount=Decimal("280000"),
            description="Готовый офис с мебелью в современном БЦ класса А",
            amenities="Ресепшн, Переговорные, Кафетерий, Охрана 24/7, Паркинг",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Пентхаус",
            address="Москва, Воробьевы Горы, ЖК Доминион, кв. 501",
            area=Decimal("195.0"),
            rooms_count=4,
            floor=25,
            total_floors=25,
            renovation_type="Люкс",
            is_furnished=True,
            monthly_rent=Decimal("420000"),
            utilities_included=True,
            deposit_amount=Decimal("840000"),
            description="Роскошный пентхаус с террасой и видом на Москва-реку",
            amenities="Терраса 50м², Панорамные окна, Сауна, Винный погреб, Консьерж",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Квартира",
            address="Москва, Сокольники, Русаковская ул., 13, кв. 41",
            area=Decimal("47.0"),
            rooms_count=1,
            floor=3,
            total_floors=9,
            renovation_type="Современный",
            is_furnished=True,
            monthly_rent=Decimal("58000"),
            utilities_included=False,
            deposit_amount=Decimal("58000"),
            description="Однушка в тихом районе рядом с парком Сокольники",
            amenities="Wi-Fi, Кондиционер, Рядом парк",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Квартира",
            address="Москва, Хорошевское шоссе, 88, кв. 156",
            area=Decimal("92.0"),
            rooms_count=3,
            floor=11,
            total_floors=20,
            renovation_type="Дизайнерский",
            is_furnished=True,
            monthly_rent=Decimal("135000"),
            utilities_included=False,
            deposit_amount=Decimal("135000"),
            description="Трехкомнатная квартира с авторским дизайном",
            amenities="Wi-Fi, Умный дом, Посудомойка, Паркинг, Консьерж",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="commercial",
            subtype="Офис",
            address="Москва, БЦ Нагатинский, 3 этаж",
            area=Decimal("55.0"),
            floor=3,
            total_floors=12,
            renovation_type="Стандарт",
            is_furnished=False,
            monthly_rent=Decimal("95000"),
            utilities_included=False,
            deposit_amount=Decimal("190000"),
            description="Офис под отделку в развивающемся районе",
            amenities="Охрана, Парковка, Рядом метро",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Студия",
            address="Москва, Дмитровское шоссе, 107, кв. 89",
            area=Decimal("29.0"),
            rooms_count=1,
            floor=7,
            total_floors=14,
            renovation_type="Современный",
            is_furnished=True,
            monthly_rent=Decimal("40000"),
            utilities_included=False,
            deposit_amount=Decimal("40000"),
            description="Удобная студия с современным ремонтом",
            amenities="Wi-Fi, Встроенная техника, Охраняемая территория",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Квартира",
            address="Москва, Мичуринский проспект, 23, кв. 201",
            area=Decimal("112.0"),
            rooms_count=4,
            floor=16,
            total_floors=24,
            renovation_type="Премиум",
            is_furnished=True,
            monthly_rent=Decimal("185000"),
            utilities_included=False,
            deposit_amount=Decimal("370000"),
            description="Просторная четырехкомнатная квартира для большой семьи",
            amenities="Гардеробная, Два санузла, Балкон, Паркинг, Детская площадка",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="commercial",
            subtype="Торговое помещение",
            address="Москва, ТК Садовод, павильон 215",
            area=Decimal("42.0"),
            floor=1,
            total_floors=2,
            renovation_type="Базовый",
            is_furnished=False,
            monthly_rent=Decimal("85000"),
            utilities_included=False,
            deposit_amount=Decimal("170000"),
            description="Торговое место в крупном торговом комплексе",
            amenities="Витрина, Складское помещение, Охрана",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Коттедж",
            address="Москва, Новорижское шоссе, КП Английский квартал, дом 7",
            area=Decimal("315.0"),
            rooms_count=6,
            floor=1,
            total_floors=3,
            renovation_type="Премиум",
            is_furnished=True,
            monthly_rent=Decimal("550000"),
            utilities_included=False,
            deposit_amount=Decimal("1100000"),
            description="Роскошный коттедж в элитном поселке на Рублевке",
            amenities="Бассейн, Сауна, Бильярдная, Гараж на 3 машины, Ландшафтный дизайн, Охрана",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Квартира",
            address="Москва, Каширское шоссе, 61, кв. 325",
            area=Decimal("63.0"),
            rooms_count=2,
            floor=19,
            total_floors=25,
            renovation_type="Евро",
            is_furnished=True,
            monthly_rent=Decimal("72000"),
            utilities_included=False,
            deposit_amount=Decimal("72000"),
            description="Двухкомнатная квартира с хорошим ремонтом",
            amenities="Wi-Fi, Кондиционер, Стиральная машина, Паркинг",
            status="available",
            published_at=datetime.now()
        ),
    ]
    db.add_all(properties)
    db.commit()
    print("✓ Properties created")

    # 5. Create User Clients (plain passwords for educational purposes)
    user_clients = [
        UserClient(
            phone="+79998887766",
            email="alex@example.com",
            password_hash="client123",  # Plain text password
            is_active=True,
            is_verified=True
        ),
        UserClient(
            phone="+79997776655",
            email="maria@example.com",
            password_hash="client123",  # Plain text password
            is_active=True,
            is_verified=True
        ),
        UserClient(
            phone="+79996665544",
            email="dmitry@example.com",
            password_hash="client123",  # Plain text password
            is_active=True,
            is_verified=True
        ),
    ]
    db.add_all(user_clients)
    db.commit()
    print("✓ User clients created")

    # 6. Create Client Profiles
    clients = [
        Client(
            user_id=1,
            full_name="Alexander Ivanov",
            date_of_birth=date(1990, 5, 15),
            phone="+79998887766",
            email="alex@example.com",
            registration_address="Moscow, Lenin Street, 25, apt 10",
            actual_address="Moscow, Lenin Street, 25, apt 10",
            workplace='LLC "TechCorp"',
            position="Senior Developer",
            monthly_income=Decimal("150000"),
            is_verified=True,
            client_type="individual",
            registration_date=date(2024, 1, 15)
        ),
        Client(
            user_id=2,
            full_name="Maria Petrova",
            date_of_birth=date(1985, 8, 22),
            phone="+79997776655",
            email="maria@example.com",
            registration_address="Moscow, Pushkin Street, 12, apt 55",
            actual_address="Moscow, Pushkin Street, 12, apt 55",
            workplace='Bank "Finance Plus"',
            position="Manager",
            monthly_income=Decimal("120000"),
            is_verified=True,
            client_type="individual",
            registration_date=date(2024, 2, 10)
        ),
        Client(
            user_id=3,
            full_name="Dmitry Smirnov",
            date_of_birth=date(1992, 3, 10),
            phone="+79996665544",
            email="dmitry@example.com",
            registration_address="Moscow, Gagarin Street, 7, apt 89",
            actual_address="Moscow, Gagarin Street, 7, apt 89",
            workplace='LLC "StartupHub"',
            position="Product Manager",
            monthly_income=Decimal("180000"),
            is_verified=True,
            client_type="individual",
            company_id=1,
            registration_date=date(2024, 3, 5)
        ),
    ]
    db.add_all(clients)
    db.commit()
    print("✓ Clients created")

    # 7. Create Applications
    applications = [
        Application(
            client_id=1,
            property_id=1,
            application_date=date.today() - timedelta(days=5),
            status="approved",
            preferred_move_in_date=date.today() + timedelta(days=7),
            lease_duration_months=12,
            notes="Looking for long-term rental"
        ),
        Application(
            client_id=2,
            property_id=2,
            application_date=date.today() - timedelta(days=3),
            status="under_review",
            preferred_move_in_date=date.today() + timedelta(days=14),
            lease_duration_months=12,
            notes="Family of 3 people"
        ),
        Application(
            client_id=3,
            property_id=5,
            application_date=date.today() - timedelta(days=10),
            status="approved",
            preferred_move_in_date=date.today() - timedelta(days=5),
            lease_duration_months=24,
            notes="Office for startup company"
        ),
    ]
    db.add_all(applications)
    db.commit()
    print("✓ Applications created")

    # 8. Create Contracts
    contracts = [
        Contract(
            contract_number="RENT-2024-001",
            client_id=3,
            property_id=7,
            employee_id=1,
            signing_date=date.today() - timedelta(days=30),
            start_date=date.today() - timedelta(days=25),
            end_date=date.today() + timedelta(days=335),
            monthly_rent=Decimal("65000"),
            deposit_amount=Decimal("65000"),
            deposit_paid=True,
            contract_status="active",
            payment_day=5,
            payment_method="Bank transfer",
            signed_electronically=True
        ),
    ]
    db.add_all(contracts)
    db.commit()
    print("✓ Contracts created")

    # 9. Create Payments
    payments = [
        Payment(
            contract_id=1,
            payment_date=date.today() - timedelta(days=25),
            amount=Decimal("65000"),
            payment_type="deposit",
            payment_method="Bank transfer",
            payment_status="completed",
            transaction_id="TRX-001-2024",
            is_late=False,
            late_days=0,
            penalty_amount=Decimal("0")
        ),
        Payment(
            contract_id=1,
            payment_date=date.today() - timedelta(days=20),
            amount=Decimal("65000"),
            payment_type="rent",
            payment_method="Bank transfer",
            payment_status="completed",
            transaction_id="TRX-002-2024",
            period_month=datetime.now().month,
            period_year=datetime.now().year,
            is_late=False,
            late_days=0,
            penalty_amount=Decimal("0")
        ),
    ]
    db.add_all(payments)
    db.commit()
    print("✓ Payments created")

    # 10. Create Additional Services
    services = [
        AdditionalService(
            name="Уборка помещения",
            description="Профессиональная уборка 1 раз в неделю",
            price=Decimal("5000"),
            unit="в месяц",
            is_active=True
        ),
        AdditionalService(
            name="Парковочное место",
            description="Подземная охраняемая парковка",
            price=Decimal("8000"),
            unit="в месяц",
            is_active=True
        ),
        AdditionalService(
            name="Интернет",
            description="Высокоскоростной интернет 100 Мбит/с",
            price=Decimal("1000"),
            unit="в месяц",
            is_active=True
        ),
        AdditionalService(
            name="Аренда мебели",
            description="Полный комплект мебели для квартиры",
            price=Decimal("15000"),
            unit="в месяц",
            is_active=True
        ),
        AdditionalService(
            name="Консьерж-сервис",
            description="Персональный консьерж 24/7",
            price=Decimal("12000"),
            unit="в месяц",
            is_active=True
        ),
        AdditionalService(
            name="Химчистка",
            description="Химчистка ковров и мебели",
            price=Decimal("3500"),
            unit="за услугу",
            is_active=True
        ),
        AdditionalService(
            name="Кабельное ТВ",
            description="Пакет из 150+ каналов",
            price=Decimal("800"),
            unit="в месяц",
            is_active=True
        ),
        AdditionalService(
            name="Вывоз мусора",
            description="Ежедневный вывоз мусора",
            price=Decimal("500"),
            unit="в месяц",
            is_active=True
        ),
        AdditionalService(
            name="Хранение вещей",
            description="Кладовка в здании 5 м²",
            price=Decimal("4000"),
            unit="в месяц",
            is_active=True
        ),
        AdditionalService(
            name="Доступ в спортзал",
            description="Фитнес-центр в здании",
            price=Decimal("6000"),
            unit="в месяц",
            is_active=True
        ),
    ]
    db.add_all(services)
    db.commit()
    print("✓ Additional services created")

    # 11. Create Contracts
    contracts = [
        Contract(
            contract_number="RENT-2025-001",
            client_id=1,
            property_id=1,
            employee_id=3,
            signing_date=date.today() - timedelta(days=60),
            start_date=date.today() - timedelta(days=50),
            end_date=date.today() + timedelta(days=315),
            monthly_rent=Decimal("75000"),
            deposit_amount=Decimal("75000"),
            deposit_paid=True,
            contract_status='active',
            payment_day=5,
            payment_method='bank_transfer',
            additional_services="Парковочное место, Интернет",
            signed_electronically=True,
            notes="Договор с физическим лицом. Клиент надежный, оплата всегда вовремя."
        ),
        Contract(
            contract_number="RENT-2025-002",
            client_id=2,
            property_id=3,
            employee_id=3,
            signing_date=date.today() - timedelta(days=90),
            start_date=date.today() - timedelta(days=80),
            end_date=date.today() + timedelta(days=285),
            monthly_rent=Decimal("95000"),
            deposit_amount=Decimal("95000"),
            deposit_paid=True,
            contract_status='active',
            payment_day=1,
            payment_method='bank_transfer',
            additional_services="Парковочное место, Уборка помещения, Интернет",
            signed_electronically=False,
            notes="Долгосрочный договор аренды с компанией."
        ),
        Contract(
            contract_number="RENT-2024-089",
            client_id=3,
            property_id=5,
            employee_id=3,
            signing_date=date.today() - timedelta(days=180),
            start_date=date.today() - timedelta(days=170),
            end_date=date.today() - timedelta(days=10),
            monthly_rent=Decimal("55000"),
            deposit_amount=Decimal("55000"),
            deposit_paid=True,
            contract_status='expired',
            payment_day=10,
            payment_method='cash',
            additional_services="Интернет",
            signed_electronically=True,
            notes="Договор истек. Клиент съехал без проблем, залог возвращен."
        ),
    ]
    db.add_all(contracts)
    db.commit()
    print("✓ Contracts created")

    # 12. Create Reviews
    reviews = [
        Review(
            client_id=1,
            property_id=1,
            rating=5,
            text="Excellent apartment! Clean, modern, and perfect location. Highly recommend!",
            review_date=date.today() - timedelta(days=2),
            is_approved=True
        ),
        Review(
            client_id=2,
            property_id=2,
            rating=4,
            text="Great apartment with beautiful views. Only minor issue with elevator sometimes.",
            review_date=date.today() - timedelta(days=5),
            is_approved=True
        ),
        Review(
            client_id=3,
            property_id=7,
            rating=5,
            text="Living here for a month already. Very comfortable and quiet neighborhood!",
            review_date=date.today() - timedelta(days=1),
            is_approved=True
        ),
    ]
    db.add_all(reviews)
    db.commit()
    print("✓ Reviews created")

    print("✅ Initial data created successfully!")
    print("\n" + "="*60)
    print("Test credentials:")
    print("="*60)
    print("Admin: login='admin', password='admin123'")
    print("Manager: login='manager1', password='manager123'")
    print("Client 1: phone='+79998887766', password='client123'")
    print("Client 2: phone='+79997776655', password='client123'")
    print("Client 3: phone='+79996665544', password='client123'")
    print("="*60)
