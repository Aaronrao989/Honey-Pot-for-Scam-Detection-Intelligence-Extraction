from fastapi import APIRouter, Header, HTTPException, Request
from app.services.conversation_manager import process_message
from app.config import settings

router = APIRouter()


# ------------------- OFFICIAL EVALUATION ROUTE -------------------
@router.post("/honeypot")
async def honeypot_endpoint(
    request: Request,
    x_api_key: str = Header(None)
):
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    try:
        body = await request.json()
    except Exception:
        body = {}

    if "sessionId" not in body or "message" not in body:
        return {
            "status": "success",
            "reply": "Okay, can you explain more?"
        }

    return process_message(body)


# ------------------- DEMO FRONTEND ROUTE (NO API KEY) -------------------
@router.post("/demo-chat")
async def demo_chat(request: Request):
    """
    This route is ONLY for demo UI.
    No API key required. Internally uses same logic.
    """
    try:
        body = await request.json()
    except Exception:
        body = {}

    return process_message(body)
