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

    # -------- Safely read JSON --------
    try:
        body = await request.json()
    except Exception:
        body = {}

    # -------- If not real payload --------
    if "sessionId" not in body or "message" not in body:
        return {
            "status": "success",
            "reply": "Okay, can you explain more?"
        }

    # -------- Real honeypot processing --------
    return process_message(body)
