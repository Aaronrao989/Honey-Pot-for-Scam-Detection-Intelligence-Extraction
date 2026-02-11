import re

# ------------------ UPI ID ------------------
UPI_PATTERN = re.compile(
    r'\b[a-zA-Z0-9.\-_]{2,}@[a-zA-Z]{2,}\b'
)

# ------------------ Phone Numbers (Indian) ------------------
# IMPORTANT: non-capturing group (?: ) so full number is returned
PHONE_PATTERN = re.compile(
    r'(?:\+91[\-\s]?)?[6-9]\d{9}\b'
)

# ------------------ Bank Account Numbers ------------------
# 9 to 18 digit sequences (after phones are removed from text)
BANK_ACCOUNT_PATTERN = re.compile(
    r'\b\d{9,18}\b'
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
