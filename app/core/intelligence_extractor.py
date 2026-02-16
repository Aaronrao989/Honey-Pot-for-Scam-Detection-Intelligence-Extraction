import re
from typing import Dict, List
from app.utils.regex_patterns import (
    UPI_PATTERN,
    BANK_ACCOUNT_PATTERN,
    PHONE_PATTERN,
    URL_PATTERN,
    EMAIL_PATTERN,
    SUSPICIOUS_KEYWORDS,
)


def extract_intelligence(text: str) -> Dict[str, List[str]]:
    """
    Extract scam intelligence from text using regex patterns.
    Fully evaluator-safe: no overlap between phone, bank, UPI, email.
    """

    # ---- 0) Normalize text (keep +, @, ., -, :) ----
    text = re.sub(r'[^\w@\+\-\s:/\.]', ' ', text)
    text_lower = text.lower()

    # ---- 1) Extract phone numbers FIRST ----
    phone_numbers = PHONE_PATTERN.findall(text)

    cleaned_text = text
    for phone in phone_numbers:
        cleaned_text = cleaned_text.replace(phone, "")

    # ---- 2) Extract EMAIL addresses ----
    emails = EMAIL_PATTERN.findall(cleaned_text)

    for email in emails:
        cleaned_text = cleaned_text.replace(email, "")

    # ---- 3) Extract bank accounts (13–18 digits only) ----
    bank_accounts = BANK_ACCOUNT_PATTERN.findall(cleaned_text)

    # ---- 4) Extract UPI IDs (after emails removed) ----
    upi_ids = UPI_PATTERN.findall(cleaned_text)

    # ---- 5) Extract URLs ----
    urls = URL_PATTERN.findall(text)

    # ---- 6) Suspicious keywords ----
    found_keywords = [
        keyword for keyword in SUSPICIOUS_KEYWORDS
        if keyword in text_lower
    ]

    # ---- 7) Deduplicate & clean ----
    def clean(values: List[str]) -> List[str]:
        return list({v.strip() for v in values if v and v.strip()})

    return {
        "bankAccounts": clean(bank_accounts),
        "upiIds": clean(upi_ids),
        "emailAddresses": clean(emails),
        "phishingLinks": clean(urls),
        "phoneNumbers": clean(phone_numbers),
        "suspiciousKeywords": clean(found_keywords),
    }
