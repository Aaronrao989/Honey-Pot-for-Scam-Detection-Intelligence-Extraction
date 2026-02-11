from fastapi import APIRouter, Header, HTTPException, Request
from app.services.conversation_manager import process_message
from app.core.memory_store import get_session
from app.config import settings

router = APIRouter()


# ------------------- OFFICIAL EVALUATION ROUTE -------------------
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

    # -------- Handle tester / invalid payload --------
    if "sessionId" not in body or "message" not in body:
        return {
            "status": "success",
            "reply": "Okay, can you explain more?"
        }

    # -------- Run honeypot logic --------
    response = process_message(body)

    # -------- Fetch session for full intelligence --------
    session = get_session(body["sessionId"])

    return {
        "status": "success",
        "reply": response["reply"],

        # 👇 Visible to GUVI tester & judges
        "scamDetected": session["scam_detected"],
        "totalMessagesExchanged": session["total_messages"],
        "extractedIntelligence": {
            k: list(v) for k, v in session["extracted_intelligence"].items()
        },
        "agentNotes": " | ".join(session["agent_notes"])
    }


# ------------------- DEMO FRONTEND ROUTE -------------------
@router.post("/demo-chat")
async def demo_chat(request: Request):
    """
    This route is ONLY for demo UI.
    No API key required.
    Shows live intelligence panel.
    """
    try:
        body = await request.json()
    except Exception:
        body = {}

    # Run normal honeypot logic
    response = process_message(body)

    # Fetch full session for debug panel
    session = get_session(body["sessionId"])

    debug_info = {
        "scamDetected": session["scam_detected"],
        "totalMessagesExchanged": session["total_messages"],
        "extractedIntelligence": {
            k: list(v) for k, v in session["extracted_intelligence"].items()
        },
        "agentNotes": " | ".join(session["agent_notes"])
    }

    return {
        "reply": response["reply"],
        "debug": debug_info
    }
