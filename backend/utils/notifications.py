import os
from typing import Optional


async def send_sms(phone: str, message: str) -> bool:
    """
    Send SMS notification
    In production, integrate with SMS service provider (e.g., Twilio, SMS.RU)
    """
    # TODO: Implement actual SMS sending
    print(f"[SMS] To: {phone}, Message: {message}")
    return True


async def send_email(to_email: str, subject: str, body: str) -> bool:
    """
    Send email notification
    In production, integrate with email service provider
    """
    # TODO: Implement actual email sending
    print(f"[EMAIL] To: {to_email}, Subject: {subject}")
    print(f"Body: {body}")
    return True


async def send_verification_code(phone: str, code: str) -> bool:
    """Send verification code via SMS"""
    message = f"Your RentFlow verification code: {code}"
    return await send_sms(phone, message)


async def send_application_notification(email: str, property_address: str, status: str) -> bool:
    """Send application status notification"""
    subject = f"Application Status Update - {status}"
    body = f"""
    Your rental application for property at {property_address} has been {status}.

    Please log in to your account for more details.

    Best regards,
    RentFlow Team
    """
    return await send_email(email, subject, body)


async def send_payment_reminder(email: str, amount: float, due_date: str) -> bool:
    """Send payment reminder"""
    subject = "Rent Payment Reminder"
    body = f"""
    This is a reminder that your rent payment of {amount} RUB is due on {due_date}.

    Please ensure timely payment to avoid late fees.

    Best regards,
    RentFlow Team
    """
    return await send_email(email, subject, body)
