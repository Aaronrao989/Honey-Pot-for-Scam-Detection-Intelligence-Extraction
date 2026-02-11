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
    Properly separates phone numbers from bank accounts and removes noise.
    """

    text_lower = text.lower()

    # ---- 1) Extract phone numbers FIRST ----
    phone_numbers = PHONE_PATTERN.findall(text)

    # Clean text so bank regex does not capture phone digits
    cleaned_text = text
    for phone in phone_numbers:
        cleaned_text = cleaned_text.replace(phone, "")

    # ---- 2) Extract bank accounts from cleaned text ----
    bank_accounts = BANK_ACCOUNT_PATTERN.findall(cleaned_text)

    # ---- 3) Extract others normally ----
    upi_ids = UPI_PATTERN.findall(text)
    urls = URL_PATTERN.findall(text)

    # ---- 4) Suspicious keywords ----
    found_keywords = [
        keyword for keyword in SUSPICIOUS_KEYWORDS
        if keyword in text_lower
    ]

    # ---- 5) Remove duplicates and empty values ----
    def clean(values: List[str]) -> List[str]:
        return list({v.strip() for v in values if v and v.strip()})

    return {
        "bankAccounts": clean(bank_accounts),
        "upiIds": clean(upi_ids),
        "phishingLinks": clean(urls),
        "phoneNumbers": clean(phone_numbers),
        "suspiciousKeywords": clean(found_keywords),
    }
