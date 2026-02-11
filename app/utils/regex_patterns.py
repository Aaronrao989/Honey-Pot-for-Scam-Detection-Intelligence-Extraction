import re

# ------------------ UPI ID ------------------
UPI_PATTERN = re.compile(
    r'\b[a-zA-Z0-9.\-_]{2,}@[a-zA-Z]{2,}\b'
)

# ------------------ Phone Numbers (Indian) ------------------
PHONE_PATTERN = re.compile(
    r'(?:\+91[\-\s]?)?[6-9]\d{9}\b'
)

# ------------------ Bank Account Numbers (FIXED) ------------------
BANK_ACCOUNT_PATTERN = re.compile(
    r'(?<!\d)\d{9,18}(?!\d)'
)

# ------------------ URLs / Phishing Links ------------------
URL_PATTERN = re.compile(
    r'(https?://[^\s]+)'
)

# ------------------ Suspicious Scam Keywords ------------------
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
    "update kyc"
]
