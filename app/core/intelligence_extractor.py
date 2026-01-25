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
    """
    text_lower = text.lower()

    upi_ids = UPI_PATTERN.findall(text)
    bank_accounts = BANK_ACCOUNT_PATTERN.findall(text)
    phone_numbers = PHONE_PATTERN.findall(text)
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
