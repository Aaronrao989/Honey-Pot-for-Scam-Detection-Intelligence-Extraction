from fastapi import APIRouter, Header, HTTPException, Request
from app.services.conversation_manager import process_message
from app.core.memory_store import get_session, delete_session
from app.db.mongo_repository import save_conversation
from app.config import settings

router = APIRouter()


# ==========================================================
# OFFICIAL EVALUATION ENDPOINT (GUVI)
# ==========================================================
@router.post("/honeypot")
async def honeypot_endpoint(
    request: Request,
    x_api_key: str = Header(None)
):
    # ---- API key validation ----
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # ---- Safe JSON read ----
    try:
        body = await request.json()
    except Exception:
        body = {}

    # ---- Handle tester pings / malformed payloads ----
    if "sessionId" not in body or "message" not in body:
        return {
            "status": "success",
            "reply": "Okay, can you explain more?"
        }

    # ---- Core honeypot logic ----
    response = process_message(body)
    session = get_session(body["sessionId"])

    return {
        "status": "success",
        "reply": response["reply"],

        # Extra fields are SAFE (GUVI ignores them)
        "scamDetected": session["scam_detected"],
        "totalMessagesExchanged": session["total_messages"],
        "extractedIntelligence": {
            k: list(v) for k, v in session["extracted_intelligence"].items()
        },
        "agentNotes": " | ".join(session["agent_notes"]),
    }


# ==========================================================
# DEMO FRONTEND ENDPOINT (NO API KEY)
# ==========================================================
@router.post("/demo-chat")
async def demo_chat(request: Request):
    try:
        body = await request.json()
    except Exception:
        body = {}

    # Guard against invalid demo requests
    if "sessionId" not in body or "message" not in body:
        return {
            "status": "success",
            "reply": "Please enter a message to start the demo.",
            "debug": {}
        }

    response = process_message(body)
    session = get_session(body["sessionId"])

    return {
        "status": "success",
        "reply": response["reply"],
        "debug": {
            "scamDetected": session["scam_detected"],
            "totalMessagesExchanged": session["total_messages"],
            "extractedIntelligence": {
                k: list(v) for k, v in session["extracted_intelligence"].items()
            },
            "agentNotes": " | ".join(session["agent_notes"]),
        },
    }


# ==========================================================
# END CHAT – SAVE & RESET SESSION (NEW FEATURE)
# ==========================================================
@router.post("/end-chat")
async def end_chat(request: Request):
    try:
        body = await request.json()
    except Exception:
        body = {}

    session_id = body.get("sessionId")
    if not session_id:
        raise HTTPException(status_code=400, detail="sessionId required")

    # If session already ended or never existed
    try:
        session = get_session(session_id)
    except Exception:
        return {
            "status": "ended",
            "sessionId": session_id,
            "message": "Session already closed"
        }

    # ---- Persist to MongoDB ----
    try:
        save_conversation(session_id, session)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to save conversation: {str(e)}"
        )

    # ---- Clear in-memory session ----
    delete_session(session_id)

    return {
        "status": "ended",
        "sessionId": session_id,
        "message": "Conversation saved and session closed"
    }
