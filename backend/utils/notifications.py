import os
from typing import Optional


async def send_sms(phone: str, message: str) -> bool:
    """
    Отправка SMS уведомления
    В продакшене интегрировать с провайдером SMS (например, Twilio, SMS.RU)
    """
    # TODO: Реализовать реальную отправку SMS
    print(f"[SMS] Кому: {phone}, Сообщение: {message}")
    return True


async def send_email(to_email: str, subject: str, body: str) -> bool:
    """
    Отправка email уведомления
    В продакшене интегрировать с провайдером email сервиса
    """
    # TODO: Реализовать реальную отправку email
    print(f"[EMAIL] Кому: {to_email}, Тема: {subject}")
    print(f"Тело: {body}")
    return True


async def send_verification_code(phone: str, code: str) -> bool:
    """Отправка кода верификации через SMS"""
    message = f"Ваш код верификации RentFlow: {code}"
    return await send_sms(phone, message)


async def send_application_notification(email: str, property_address: str, status: str) -> bool:
    """Отправка уведомления о статусе заявки"""
    subject = f"Обновление статуса заявки - {status}"
    body = f"""
    Ваша заявка на аренду объекта по адресу {property_address} получила статус: {status}.

    Пожалуйста, войдите в свой аккаунт для получения дополнительной информации.

    С уважением,
    Команда RentFlow
    """
    return await send_email(email, subject, body)


async def send_payment_reminder(email: str, amount: float, due_date: str) -> bool:
    """Отправка напоминания о платеже"""
    subject = "Напоминание об оплате аренды"
    body = f"""
    Это напоминание о том, что ваш платеж за аренду в размере {amount} руб. должен быть произведен до {due_date}.

    Пожалуйста, обеспечьте своевременную оплату во избежание штрафов.

    С уважением,
    Команда RentFlow
    """
    return await send_email(email, subject, body)
