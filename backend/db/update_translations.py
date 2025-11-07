"""Скрипт для обновления существующих записей на русский язык"""
from sqlalchemy.orm import Session
from db.database import SessionLocal, engine
from db.models import Review, AdditionalService
from datetime import date


def update_reviews_to_russian(db: Session):
    """Обновление отзывов на русский язык"""

    # Словарь для перевода отзывов
    review_translations = {
        "Excellent apartment! Clean, modern, and perfect location. Highly recommend!":
            "Отличная квартира! Чистая, современная и идеальное расположение. Очень рекомендую!",
        "Great apartment with beautiful views. Only minor issue with elevator sometimes.":
            "Прекрасная квартира с красивым видом. Единственная небольшая проблема - иногда лифт.",
        "Living here for a month already. Very comfortable and quiet neighborhood!":
            "Живу здесь уже месяц. Очень комфортный и тихий район!",
        "Nice place to stay. Would recommend!":
            "Приятное место для проживания. Рекомендую!",
        "Perfect location and amenities":
            "Идеальное расположение и удобства",
        "Good value for money":
            "Хорошее соотношение цены и качества"
    }

    # Получаем все отзывы
    reviews = db.query(Review).all()
    updated_count = 0

    for review in reviews:
        if review.text in review_translations:
            review.text = review_translations[review.text]
            updated_count += 1

    if updated_count > 0:
        db.commit()
        print(f"✓ Обновлено отзывов: {updated_count}")
    else:
        print("✓ Отзывы уже на русском языке или не найдены для перевода")


def update_services_to_russian(db: Session):
    """Обновление услуг на русский язык"""

    # Словарь для перевода названий услуг
    service_name_translations = {
        "Parking space": "Парковочное место",
        "Underground parking": "Подземная парковка",
        "Cleaning service": "Уборка помещения",
        "Internet": "Интернет",
        "Cable TV": "Кабельное ТВ",
        "Furniture rental": "Аренда мебели",
        "Full furniture package": "Аренда мебели",
        "Concierge service": "Консьерж-сервис",
        "Dry cleaning": "Химчистка",
        "Trash removal": "Вывоз мусора",
        "Storage": "Хранение вещей",
        "Gym access": "Доступ в спортзал"
    }

    # Словарь для перевода описаний услуг
    service_description_translations = {
        "Underground parking": "Подземная охраняемая парковка",
        "Secure underground parking": "Подземная охраняемая парковка",
        "Professional cleaning once a week": "Профессиональная уборка 1 раз в неделю",
        "High-speed internet 100 Mbps": "Высокоскоростной интернет 100 Мбит/с",
        "Cable TV package with 150+ channels": "Пакет из 150+ каналов",
        "Full apartment furniture set": "Полный комплект мебели для квартиры",
        "Full furniture package": "Полный комплект мебели для квартиры",
        "Personal concierge 24/7": "Персональный консьерж 24/7",
        "Carpet and furniture dry cleaning": "Химчистка ковров и мебели",
        "Daily trash removal": "Ежедневный вывоз мусора",
        "5 m² storage in building": "Кладовка в здании 5 м²",
        "Fitness center in building": "Фитнес-центр в здании"
    }

    # Словарь для перевода единиц измерения
    unit_translations = {
        "per month": "в месяц",
        "per service": "за услугу",
        "monthly": "в месяц"
    }

    # Получаем все услуги
    services = db.query(AdditionalService).all()
    updated_count = 0

    for service in services:
        updated = False
        if service.name in service_name_translations:
            service.name = service_name_translations[service.name]
            updated = True
        if service.description in service_description_translations:
            service.description = service_description_translations[service.description]
            updated = True
        if service.unit in unit_translations:
            service.unit = unit_translations[service.unit]
            updated = True
        if updated:
            updated_count += 1

    if updated_count > 0:
        db.commit()
        print(f"✓ Обновлено услуг: {updated_count}")
    else:
        print("✓ Услуги уже на русском языке или не найдены для перевода")


def main():
    """Основная функция для запуска обновлений"""
    print("="*60)
    print("Обновление данных на русский язык")
    print("="*60)

    db = SessionLocal()
    try:
        update_reviews_to_russian(db)
        update_services_to_russian(db)
        print("="*60)
        print("✅ Обновление завершено успешно!")
        print("="*60)
    except Exception as e:
        print(f"❌ Ошибка при обновлении: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    main()
