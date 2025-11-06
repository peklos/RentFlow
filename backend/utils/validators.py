import re
from typing import Optional


def validate_phone(phone: str) -> bool:
    """Validate phone number format"""
    # Russian phone format: +7XXXXXXXXXX or 8XXXXXXXXXX
    pattern = r'^(\+7|8)\d{10}$'
    return bool(re.match(pattern, phone))


def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_inn(inn: str) -> bool:
    """Validate Russian INN (taxpayer identification number)"""
    # INN can be 10 or 12 digits
    return bool(re.match(r'^\d{10}$|^\d{12}$', inn))


def validate_passport(series: str, number: str) -> bool:
    """Validate Russian passport format"""
    # Series: 4 digits, Number: 6 digits
    return bool(re.match(r'^\d{4}$', series) and re.match(r'^\d{6}$', number))


def normalize_phone(phone: str) -> str:
    """Normalize phone number to +7XXXXXXXXXX format"""
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone)

    # If starts with 8, replace with 7
    if digits.startswith('8'):
        digits = '7' + digits[1:]

    # Add + if not present
    if not digits.startswith('+'):
        digits = '+' + digits

    return digits
