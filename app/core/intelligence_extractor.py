from typing import Dict, List
from app.utils.regex_patterns import (
    UPI_PATTERN,
    BANK_ACCOUNT_PATTERN,
    PHONE_PATTERN,
    URL_PATTERN,
    SUSPICIOUS_KEYWORDS,
)


def extract_intelligence(text: str) -> Dict[str, List[str]]:
    """
    Extract scam intelligence from text using regex patterns.
    Handles overlap between phone numbers and bank accounts.
    """
    text_lower = text.lower()

    # ---- Extract phone numbers FIRST ----
    phone_numbers = PHONE_PATTERN.findall(text)

    # Remove phones from text before checking bank accounts
    cleaned_text = text
    for phone in phone_numbers:
        cleaned_text = cleaned_text.replace(phone, "")

    # ---- Now extract bank accounts safely ----
    bank_accounts = BANK_ACCOUNT_PATTERN.findall(cleaned_text)

    # ---- Other patterns ----
    upi_ids = UPI_PATTERN.findall(text)
    urls = URL_PATTERN.findall(text)

    found_keywords = [
        keyword for keyword in SUSPICIOUS_KEYWORDS
        if keyword in text_lower
    ]

    return {
        "bankAccounts": bank_accounts,
        "upiIds": upi_ids,
        "phishingLinks": urls,
        "phoneNumbers": phone_numbers,
        "suspiciousKeywords": found_keywords,
    }
