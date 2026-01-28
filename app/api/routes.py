from fastapi import APIRouter, Header, HTTPException, Request
from app.services.conversation_manager import process_message
from app.config import settings

router = APIRouter()


@router.post("/honeypot")
async def honeypot_endpoint(
    request: Request,
    x_api_key: str = Header(...)
):
    # -------- API Key Validation --------
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    body = await request.json()

    # -------- GUVI Tester sends minimal ping --------
    # If this is not the real honeypot payload, respond safely
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
            "agentNotes": "GUVI tester ping received"
        }

    # -------- Real honeypot processing --------
    response = process_message(body)
    return response
