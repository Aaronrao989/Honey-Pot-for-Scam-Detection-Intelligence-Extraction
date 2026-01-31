from fastapi import APIRouter, HTTPException, Request
from app.services.conversation_manager import process_message
from app.config import settings

router = APIRouter()


@router.post("/honeypot")
async def honeypot_endpoint(request: Request):

    # -------- Flexible API Key Reading --------
    api_key = (
        request.headers.get("x-api-key")
        or request.headers.get("X-API-KEY")
        or request.headers.get("x_api_key")
    )

    if api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # -------- Safely read JSON (prevents 500 errors) --------
    try:
        body = await request.json()
    except Exception:
        body = {}

    # -------- GUVI tester / bots / empty requests --------
    if "sessionId" not in body or "message" not in body:
        return {
            "status": "success",
            "scamDetected": False,
            "engagementMetrics": {
                "engagementDurationSeconds": 0,
                "totalMessagesExchanged": 0
            },
            "extractedIntelligence": {
                "bankAccounts": [],
                "upiIds": [],
                "phishingLinks": [],
                "phoneNumbers": [],
                "suspiciousKeywords": []
            },
            "agentNotes": "Non-standard request handled safely"
        }

    # -------- Real honeypot processing --------
    response = process_message(body)
    return response
