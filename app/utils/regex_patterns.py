import re

# ------------------ PHONE NUMBERS ------------------
# Matches:
# +91 9876543210
# +919876543210
# 9876543210
PHONE_PATTERN = re.compile(
    r'(?:\+91[\-\s]?)?[6-9]\d{9}\b'
)

# ------------------ BANK ACCOUNT NUMBERS ------------------
# Strictly 13–18 digits (prevents phone overlap)
BANK_ACCOUNT_PATTERN = re.compile(
    r'(?<!\d)\d{13,18}(?!\d)'
)

# ------------------ UPI IDs ------------------
# Matches UPI IDs like name@bank
# EXCLUDES emails (no dot in domain)
UPI_PATTERN = re.compile(
    r'\b[a-zA-Z0-9._-]{2,}@[a-zA-Z]{2,}\b'
)

# ------------------ EMAIL ADDRESSES ------------------
EMAIL_PATTERN = re.compile(
    r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
)

# ------------------ URLs / PHISHING LINKS ------------------
URL_PATTERN = re.compile(
    r'https?://[^\s]+'
)

# ------------------ SUSPICIOUS KEYWORDS ------------------
SUSPICIOUS_KEYWORDS = [
    "urgent",
    "verify now",
    "account blocked",
    "suspended",
    "limited time",
    "click link",
    "share otp",
    "upi id",
    "bank details",
    "prize",
    "reward",
    "lottery",
    "refund",
    "kyc",
    "immediately",
    "update kyc"
]
