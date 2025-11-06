from sqlalchemy.orm import Session
from db.models import (
    Position, Employee, Company, Property, Client, UserClient,
    Application, Contract, Payment, AdditionalService, Review
)
from datetime import date, datetime, timedelta
from decimal import Decimal


def create_initial_data(db: Session):
    """Создание начальных тестовых данных для базы данных"""

    # Проверка существования данных
    if db.query(Position).first():
        print("Начальные данные уже существуют, пропускаем...")
        return

    print("Создание начальных данных...")

    # 1. Создание должностей
    positions = [
        Position(name="Администратор", description="Системный администратор", access_level=10),
        Position(name="Менеджер", description="Менеджер по недвижимости", access_level=5),
        Position(name="Агент", description="Агент по аренде", access_level=3),
    ]
    db.add_all(positions)
    db.commit()
    print("✓ Должности созданы")

    # 2. Создание сотрудников (простые пароли для учебных целей)
    employees = [
        Employee(
            login="admin",
            password_hash="admin123",  # Простой текстовый пароль
            full_name="Администратор Системы",
            position_id=1,
            phone="+79991111111",
            email="admin@rentflow.com",
            is_active=True,
            hire_date=date(2024, 1, 1)
        ),
        Employee(
            login="manager1",
            password_hash="manager123",  # Простой текстовый пароль
            full_name="Иван Петров",
            position_id=2,
            phone="+79992222222",
            email="manager@rentflow.com",
            is_active=True,
            hire_date=date(2024, 2, 1)
        ),
    ]
    db.add_all(employees)
    db.commit()
    print("✓ Сотрудники созданы")

    # 3. Создание компаний
    companies = [
        Company(
            name='ООО "Самолет Плюс"',
            inn="7712345678",
            legal_address="Москва, Красная площадь, 1"
        ),
        Company(
            name='ООО "Недвижимость XXI"',
            inn="7723456789",
            legal_address="Москва, ул. Тверская, 10"
        ),
    ]
    db.add_all(companies)
    db.commit()
    print("✓ Компании созданы")

    # 4. Создание объектов недвижимости
    properties = [
        # Жилая недвижимость
        Property(
            type="residential",
            subtype="Квартира",
            address="Москва, ул. Арбат, 15, кв. 42",
            area=Decimal("75.5"),
            rooms_count=2,
            floor=5,
            total_floors=12,
            renovation_type="Современный",
            is_furnished=True,
            monthly_rent=Decimal("80000"),
            utilities_included=False,
            deposit_amount=Decimal("80000"),
            description="Уютная 2-комнатная квартира в центре города с современным ремонтом",
            amenities="Wi-Fi, Кондиционер, Стиральная машина, Посудомоечная машина",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Пентхаус",
            address="Москва, Ленинский проспект, 45, кв. 120",
            area=Decimal("120.0"),
            rooms_count=3,
            floor=10,
            total_floors=16,
            renovation_type="Премиум",
            is_furnished=True,
            monthly_rent=Decimal("150000"),
            utilities_included=False,
            deposit_amount=Decimal("150000"),
            description="Роскошная 3-комнатная квартира с панорамным видом",
            amenities="Wi-Fi, Кондиционер, Умный дом, Парковка",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Студия",
            address="Москва, ул. Бауманская, 23, кв. 5",
            area=Decimal("35.0"),
            rooms_count=1,
            floor=3,
            total_floors=9,
            renovation_type="Стандарт",
            is_furnished=True,
            monthly_rent=Decimal("45000"),
            utilities_included=False,
            deposit_amount=Decimal("45000"),
            description="Компактная студия рядом со станцией метро",
            amenities="Wi-Fi, Кухонная техника",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Таунхаус",
            address="Москва, Кутузовский проспект, 12, кв. 78",
            area=Decimal("95.0"),
            rooms_count=2,
            floor=15,
            total_floors=25,
            renovation_type="Современный",
            is_furnished=False,
            monthly_rent=Decimal("100000"),
            utilities_included=False,
            deposit_amount=Decimal("100000"),
            description="Просторная квартира в престижном районе",
            amenities="Консьерж, Спортзал, Подземная парковка",
            status="available",
            published_at=datetime.now()
        ),
        # Коммерческая недвижимость
        Property(
            type="commercial",
            subtype="Офис",
            address="Москва, Бизнес Центр Башня, 5 этаж",
            area=Decimal("200.0"),
            floor=5,
            total_floors=20,
            renovation_type="Бизнес-класс",
            is_furnished=True,
            monthly_rent=Decimal("300000"),
            utilities_included=True,
            deposit_amount=Decimal("600000"),
            description="Современное офисное помещение в деловом районе",
            amenities="Ресепшн, Переговорные комнаты, Парковка, Охрана",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="commercial",
            subtype="Торговое помещение",
            address="Москва, ТЦ Мега, Первый этаж",
            area=Decimal("80.0"),
            floor=1,
            total_floors=3,
            renovation_type="Коммерческий",
            is_furnished=False,
            monthly_rent=Decimal("250000"),
            utilities_included=False,
            deposit_amount=Decimal("500000"),
            description="Торговая площадь в популярном торговом центре",
            amenities="Высокая проходимость, Погрузочная зона",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Квартира",
            address="Москва, Проспект Мира, 88, кв. 202",
            area=Decimal("60.0"),
            rooms_count=2,
            floor=8,
            total_floors=14,
            renovation_type="Стандарт",
            is_furnished=True,
            monthly_rent=Decimal("65000"),
            utilities_included=False,
            deposit_amount=Decimal("65000"),
            description="Комфортная квартира рядом с ВДНХ",
            amenities="Балкон, Интернет, Кабельное ТВ",
            status="rented",
            published_at=datetime.now() - timedelta(days=30)
        ),
        Property(
            type="residential",
            subtype="Коттедж",
            address="Москва, Москва-Сити, Башня Федерация, кв. 501",
            area=Decimal("250.0"),
            rooms_count=4,
            floor=50,
            total_floors=50,
            renovation_type="Люкс",
            is_furnished=True,
            monthly_rent=Decimal("500000"),
            utilities_included=True,
            deposit_amount=Decimal("1000000"),
            description="Эксклюзивный пентхаус с захватывающим видом",
            amenities="Частный лифт, Терраса, Умный дом, Консьерж, Спа",
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
        # Новые объекты
        Property(
            type="residential",
            subtype="Студия",
            address="Москва, Сходненская ул., 52, кв. 18",
            area=Decimal("30.0"),
            rooms_count=1,
            floor=5,
            total_floors=12,
            renovation_type="Современный",
            is_furnished=True,
            monthly_rent=Decimal("39000"),
            utilities_included=False,
            deposit_amount=Decimal("39000"),
            description="Светлая студия в новом доме, отличная транспортная доступность",
            amenities="Wi-Fi, Кондиционер, Встроенная кухня, Охрана",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Квартира",
            address="Москва, Комсомольский проспект, 38, кв. 142",
            area=Decimal("78.0"),
            rooms_count=3,
            floor=8,
            total_floors=17,
            renovation_type="Евро",
            is_furnished=True,
            monthly_rent=Decimal("105000"),
            utilities_included=False,
            deposit_amount=Decimal("105000"),
            description="Трехкомнатная квартира для семьи, близко к паркам и школам",
            amenities="Wi-Fi, Балкон, Стиральная машина, Посудомойка, Детская площадка",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Пентхаус",
            address="Москва, Пресненская наб., 12, кв. 601",
            area=Decimal("210.0"),
            rooms_count=5,
            floor=30,
            total_floors=30,
            renovation_type="Люкс",
            is_furnished=True,
            monthly_rent=Decimal("480000"),
            utilities_included=True,
            deposit_amount=Decimal("960000"),
            description="Премиальный пентхаус с видом на Москва-реку и город",
            amenities="Терраса, Джакузи, Сауна, Винный шкаф, Умный дом, Консьерж 24/7",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="commercial",
            subtype="Офис",
            address="Москва, БЦ Кристалл, 7 этаж",
            area=Decimal("95.0"),
            floor=7,
            total_floors=14,
            renovation_type="Бизнес-класс",
            is_furnished=True,
            monthly_rent=Decimal("155000"),
            utilities_included=True,
            deposit_amount=Decimal("310000"),
            description="Современный офис с панорамными окнами",
            amenities="Ресепшн, Конференц-залы, Кухня, Паркинг, Охрана 24/7",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Квартира",
            address="Москва, Университетский проспект, 19, кв. 87",
            area=Decimal("55.0"),
            rooms_count=2,
            floor=4,
            total_floors=9,
            renovation_type="Стандарт",
            is_furnished=True,
            monthly_rent=Decimal("62000"),
            utilities_included=False,
            deposit_amount=Decimal("62000"),
            description="Уютная двушка рядом с МГУ, идеально для студентов и молодых специалистов",
            amenities="Wi-Fi, Балкон, Интернет, Близко к метро",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Студия",
            address="Москва, Щелковское шоссе, 77, кв. 201",
            area=Decimal("27.0"),
            rooms_count=1,
            floor=10,
            total_floors=16,
            renovation_type="Современный",
            is_furnished=True,
            monthly_rent=Decimal("36000"),
            utilities_included=False,
            deposit_amount=Decimal("36000"),
            description="Бюджетная студия для одного человека",
            amenities="Wi-Fi, Кухонная техника, Охраняемая территория",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Квартира",
            address="Москва, Остоженка ул., 7, кв. 25",
            area=Decimal("140.0"),
            rooms_count=4,
            floor=3,
            total_floors=7,
            renovation_type="Премиум",
            is_furnished=True,
            monthly_rent=Decimal("280000"),
            utilities_included=False,
            deposit_amount=Decimal("560000"),
            description="Четырехкомнатная квартира в историческом центре Москвы",
            amenities="Камин, Высокие потолки, Антикварная мебель, Паркинг, Консьерж",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="commercial",
            subtype="Торговое помещение",
            address="Москва, ТЦ Авиапарк, 1 этаж",
            area=Decimal("52.0"),
            floor=1,
            total_floors=4,
            renovation_type="Коммерческий",
            is_furnished=False,
            monthly_rent=Decimal("180000"),
            utilities_included=False,
            deposit_amount=Decimal("360000"),
            description="Торговая точка в крупнейшем ТЦ Европы",
            amenities="Витрина, Высокая проходимость, Склад, Вентиляция",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Квартира",
            address="Москва, Ботанический сад, ул. Лазоревая, 3, кв. 112",
            area=Decimal("70.0"),
            rooms_count=2,
            floor=14,
            total_floors=20,
            renovation_type="Современный",
            is_furnished=True,
            monthly_rent=Decimal("82000"),
            utilities_included=False,
            deposit_amount=Decimal("82000"),
            description="Просторная квартира с видом на Ботанический сад",
            amenities="Wi-Fi, Балкон, Кондиционер, Паркинг, Рядом парк",
            status="available",
            published_at=datetime.now()
        ),
        Property(
            type="residential",
            subtype="Таунхаус",
            address="Москва, Рублевское шоссе, КП Жуковка, дом 22",
            area=Decimal("280.0"),
            rooms_count=6,
            floor=1,
            total_floors=3,
            renovation_type="Премиум",
            is_furnished=True,
            monthly_rent=Decimal("420000"),
            utilities_included=False,
            deposit_amount=Decimal("840000"),
            description="Роскошный таунхаус в элитном поселке на Рублевке",
            amenities="Бассейн, Сауна, Гараж на 3 авто, Ландшафтный дизайн, Охрана, Детская площадка",
            status="available",
            published_at=datetime.now()
        ),
    ]
    db.add_all(properties)
    db.commit()
    print("✓ Объекты недвижимости созданы")

    # 5. Создание учетных записей клиентов (простые пароли для учебных целей)
    user_clients = [
        UserClient(
            phone="+79998887766",
            email="alex@example.com",
            password_hash="client123",  # Простой текстовый пароль
            is_active=True,
            is_verified=True
        ),
        UserClient(
            phone="+79997776655",
            email="maria@example.com",
            password_hash="client123",  # Простой текстовый пароль
            is_active=True,
            is_verified=True
        ),
        UserClient(
            phone="+79996665544",
            email="dmitry@example.com",
            password_hash="client123",  # Простой текстовый пароль
            is_active=True,
            is_verified=True
        ),
    ]
    db.add_all(user_clients)
    db.commit()
    print("✓ Учетные записи клиентов созданы")

    # 6. Создание профилей клиентов
    clients = [
        Client(
            user_id=1,
            full_name="Александр Иванов",
            date_of_birth=date(1990, 5, 15),
            phone="+79998887766",
            email="alex@example.com",
            registration_address="Москва, ул. Ленина, 25, кв. 10",
            actual_address="Москва, ул. Ленина, 25, кв. 10",
            workplace='ООО "ТехКорп"',
            position="Старший разработчик",
            monthly_income=Decimal("150000"),
            is_verified=True,
            client_type="individual",
            registration_date=date(2024, 1, 15)
        ),
        Client(
            user_id=2,
            full_name="Мария Петрова",
            date_of_birth=date(1985, 8, 22),
            phone="+79997776655",
            email="maria@example.com",
            registration_address="Москва, ул. Пушкина, 12, кв. 55",
            actual_address="Москва, ул. Пушкина, 12, кв. 55",
            workplace='Банк "Финанс Плюс"',
            position="Менеджер",
            monthly_income=Decimal("120000"),
            is_verified=True,
            client_type="individual",
            registration_date=date(2024, 2, 10)
        ),
        Client(
            user_id=3,
            full_name="Дмитрий Смирнов",
            date_of_birth=date(1992, 3, 10),
            phone="+79996665544",
            email="dmitry@example.com",
            registration_address="Москва, ул. Гагарина, 7, кв. 89",
            actual_address="Москва, ул. Гагарина, 7, кв. 89",
            workplace='ООО "СтартапХаб"',
            position="Менеджер продукта",
            monthly_income=Decimal("180000"),
            is_verified=True,
            client_type="individual",
            company_id=1,
            registration_date=date(2024, 3, 5)
        ),
    ]
    db.add_all(clients)
    db.commit()
    print("✓ Клиенты созданы")

    # 7. Создание заявок
    applications = [
        Application(
            client_id=1,
            property_id=1,
            application_date=date.today() - timedelta(days=5),
            status="approved",
            preferred_move_in_date=date.today() + timedelta(days=7),
            lease_duration_months=12,
            notes="Ищу долгосрочную аренду"
        ),
        Application(
            client_id=2,
            property_id=2,
            application_date=date.today() - timedelta(days=3),
            status="under_review",
            preferred_move_in_date=date.today() + timedelta(days=14),
            lease_duration_months=12,
            notes="Семья из 3 человек"
        ),
        Application(
            client_id=3,
            property_id=5,
            application_date=date.today() - timedelta(days=10),
            status="approved",
            preferred_move_in_date=date.today() - timedelta(days=5),
            lease_duration_months=24,
            notes="Офис для стартап компании"
        ),
    ]
    db.add_all(applications)
    db.commit()
    print("✓ Заявки созданы")

    # 8. Создание контрактов
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
            payment_method="Банковский перевод",
            signed_electronically=True
        ),
    ]
    db.add_all(contracts)
    db.commit()
    print("✓ Контракты созданы")

    # 9. Создание платежей
    payments = [
        Payment(
            contract_id=1,
            payment_date=date.today() - timedelta(days=25),
            amount=Decimal("65000"),
            payment_type="deposit",
            payment_method="Банковский перевод",
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
            payment_method="Банковский перевод",
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
    print("✓ Платежи созданы")

    # 10. Создание дополнительных услуг
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
    print("✓ Дополнительные услуги созданы")

    # 11. Создание дополнительных контрактов
    contracts = [
        Contract(
            contract_number="RENT-2025-001",
            client_id=1,
            property_id=1,
            employee_id=1,
            signing_date=date.today() - timedelta(days=60),
            start_date=date.today() - timedelta(days=50),
            end_date=date.today() + timedelta(days=315),
            monthly_rent=Decimal("80000"),
            deposit_amount=Decimal("80000"),
            deposit_paid=True,
            contract_status='active',
            payment_day=5,
            payment_method='Банковский перевод',
            additional_services="Парковочное место, Интернет",
            signed_electronically=True,
            notes="Договор с физическим лицом. Клиент надежный, оплата всегда вовремя."
        ),
        Contract(
            contract_number="RENT-2025-003",
            client_id=1,
            property_id=9,
            employee_id=1,
            signing_date=date.today() - timedelta(days=120),
            start_date=date.today() - timedelta(days=110),
            end_date=date.today() + timedelta(days=255),
            monthly_rent=Decimal("55000"),
            deposit_amount=Decimal("55000"),
            deposit_paid=True,
            contract_status='active',
            payment_day=10,
            payment_method='Банковский перевод',
            additional_services="Интернет",
            signed_electronically=True,
            notes="Квартира для родственников клиента."
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
            payment_method='Банковский перевод',
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
            payment_method='Наличные',
            additional_services="Интернет",
            signed_electronically=True,
            notes="Договор истек. Клиент съехал без проблем, залог возвращен."
        ),
    ]
    db.add_all(contracts)
    db.commit()
    print("✓ Дополнительные контракты созданы")

    # 12. Создание отзывов
    reviews = [
        Review(
            client_id=1,
            property_id=1,
            rating=5,
            text="Отличная квартира! Чистая, современная и идеальное расположение. Очень рекомендую!",
            review_date=date.today() - timedelta(days=2),
            is_approved=True
        ),
        Review(
            client_id=2,
            property_id=2,
            rating=4,
            text="Прекрасная квартира с красивым видом. Единственная небольшая проблема - иногда лифт.",
            review_date=date.today() - timedelta(days=5),
            is_approved=True
        ),
        Review(
            client_id=3,
            property_id=7,
            rating=5,
            text="Живу здесь уже месяц. Очень комфортный и тихий район!",
            review_date=date.today() - timedelta(days=1),
            is_approved=True
        ),
    ]
    db.add_all(reviews)
    db.commit()
    print("✓ Отзывы созданы")

    print("✅ Начальные данные успешно созданы!")
    print("\n" + "="*60)
    print("Тестовые учетные данные:")
    print("="*60)
    print("Админ: login='admin', password='admin123'")
    print("Менеджер: login='manager1', password='manager123'")
    print("Клиент 1: phone='+79998887766', password='client123'")
    print("Клиент 2: phone='+79997776655', password='client123'")
    print("Клиент 3: phone='+79996665544', password='client123'")
    print("="*60)
