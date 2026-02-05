from fastapi import APIRouter, Header, HTTPException, Request
from app.services.conversation_manager import process_message
from app.config import settings

router = APIRouter()


@router.post("/honeypot")
async def honeypot_endpoint(
    request: Request,
    x_api_key: str = Header(None)
):
    # -------- API Key Validation --------
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # -------- Safely read JSON --------
    try:
        body = await request.json()
    except Exception:
        body = {}

    # -------- If not real payload, return safe reply --------
    if "sessionId" not in body or "message" not in body:
        return {
            "status": "success",
            "reply": "Okay, can you explain more?"
        }

    # -------- Real honeypot processing --------
    return process_message(body)
