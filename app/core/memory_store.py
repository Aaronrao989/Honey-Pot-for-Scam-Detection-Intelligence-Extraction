from typing import Dict, Any
from datetime import datetime

# In-memory store (perfect for hackathon)
SESSION_STORE: Dict[str, Dict[str, Any]] = {}


def get_session(session_id: str) -> Dict[str, Any]:
    """
    Fetch existing session or create a new one.
    """
    if session_id not in SESSION_STORE:
        SESSION_STORE[session_id] = {
            "start_time": datetime.utcnow(),
            "messages": [],
            "scam_detected": False,
            "extracted_intelligence": {
                "bankAccounts": set(),
                "upiIds": set(),
                "phishingLinks": set(),
                "phoneNumbers": set(),
                "suspiciousKeywords": set(),
            },
            "agent_notes": [],
            "total_messages": 0,
            "callback_sent": False,
        }

    return SESSION_STORE[session_id]


def update_session(session_id: str, data: Dict[str, Any]) -> None:
    """
    Update session data.
    """
    SESSION_STORE[session_id].update(data)


def append_message(session_id: str, message: Dict[str, Any]) -> None:
    """
    Add message to session history.
    """
    SESSION_STORE[session_id]["messages"].append(message)
    SESSION_STORE[session_id]["total_messages"] += 1


def add_intelligence(session_id: str, intel_type: str, values) -> None:
    """
    Add extracted intelligence without duplicates.
    """
    if intel_type in SESSION_STORE[session_id]["extracted_intelligence"]:
        SESSION_STORE[session_id]["extracted_intelligence"][intel_type].update(values)


def add_agent_note(session_id: str, note: str) -> None:
    """
    Add internal agent reasoning note.
    """
    SESSION_STORE[session_id]["agent_notes"].append(note)


# ================== NEW FUNCTION ==================
def delete_session(session_id: str) -> None:
    """
    Completely remove a session from memory.
    Called when user clicks 'End Chat'.
    """
    if session_id in SESSION_STORE:
        del SESSION_STORE[session_id]
