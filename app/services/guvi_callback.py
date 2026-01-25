import requests
from app.config import settings


def send_final_result(payload: dict) -> bool:
    """
    Sends the final extracted intelligence to GUVI evaluation endpoint.
    Returns True if successful.
    """
    try:
        response = requests.post(
            settings.GUVI_CALLBACK_URL,
            json=payload,
            timeout=settings.CALLBACK_TIMEOUT_SECONDS,
        )

        return response.status_code == 200

    except Exception as e:
        print(f"[GUVI CALLBACK ERROR] {e}")
        return False
