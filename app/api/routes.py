from fastapi import APIRouter, Header, HTTPException, Request
from app.services.conversation_manager import process_message
from app.core.memory_store import get_session, delete_session
from app.db.mongo_repository import save_conversation
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

    response = process_message(body)
    session = get_session(body["sessionId"])

    return {
        "status": "success",
        "reply": response["reply"],
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
    try:
        body = await request.json()
    except Exception:
        body = {}

    response = process_message(body)
    session = get_session(body["sessionId"])

    return {
        "reply": response["reply"],
        "debug": {
            "scamDetected": session["scam_detected"],
            "totalMessagesExchanged": session["total_messages"],
            "extractedIntelligence": {
                k: list(v) for k, v in session["extracted_intelligence"].items()
            },
            "agentNotes": " | ".join(session["agent_notes"])
        }
    }


# ------------------- END CHAT (NEW FEATURE) -------------------
@router.post("/end-chat")
async def end_chat(request: Request):
    try:
        body = await request.json()
    except Exception:
        body = {}

    session_id = body.get("sessionId")
    if not session_id:
        raise HTTPException(status_code=400, detail="sessionId required")

    session = get_session(session_id)

    # Save to MongoDB
    save_conversation(session_id, session)

    # Clear in-memory session
    delete_session(session_id)

    return {
        "status": "ended",
        "sessionId": session_id,
        "message": "Conversation saved and session closed"
    }
