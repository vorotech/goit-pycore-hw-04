"""Module for handling commands."""

import re

# Phonebook where key is name and value is phone number
contacts = {}

class ContactError(Exception):
    """Custom exception for contact errors."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

def add_contact(name: str, phone: str) -> None:
    """Adds a contact to the phonebook."""
    if name in contacts:
        raise ContactError("Contact already exists.")

    contacts[name] = _normalize_phone(phone)

def change_contact(name: str, phone: str) -> None:
    """Change a contact."""
    if name not in contacts:
        raise ContactError("No such contact.")

    contacts[name] = _normalize_phone(phone)

def get_phone(name: str) -> str:
    """Gets a phone number."""
    if name not in contacts:
        raise ContactError("No such contact.")

    return contacts[name]

def get_all_contacts() -> dict:
    """Gets all contacts."""
    return contacts


def _normalize_phone(phone_number: str, country_code = "38") -> str:
    """Normalizes phone number by removing all non-digit characters
    or `+` and adding country code if it is missing.

    Args:
        phone_number (str): Phone nummber to normalize.

    Raises:
        PhoneBookError: If phone number length is not valid

    Returns:
        str: Narmonized phone number.
    """
    pattern = r"[+\d]"
    phone_number = "".join(re.findall(pattern, phone_number))

    if not phone_number.startswith("+"):
        phone_number = re.sub(fr"^({country_code})?", f"+{country_code}", phone_number)

    if len(phone_number) != 13:
        raise ContactError("Invalid phone number.")

    return phone_number
