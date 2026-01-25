from groq import Groq
from app.config import settings
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


PERSONA_PROMPT = """
You are a normal Indian mobile user who is not very tech-savvy.

Behave like a real person chatting over SMS/WhatsApp.

Goals:
- Never reveal you suspect a scam
- Act confused, scared, greedy, or obedient
- Ask questions so the scammer reveals details (UPI, links, numbers)
- Keep responses short (1–2 sentences)
"""


STRATEGY_HINTS = {
    "scared": "You are scared your bank account will be blocked. Ask what to do.",
    "greedy": "You are excited about the reward. Ask how to claim it.",
    "obedient": "You trust them. Ask for steps.",
    "link_issue": "Say the link is not opening.",
    "otp_problem": "Say OTP not received.",
    "confused_delay": "Act confused and ask them to explain slowly.",
    "neutral_confused": "Say you don’t understand and ask basic questions."
}


def generate_reply(strategy: str, conversation_history: list) -> str:
    strategy_hint = STRATEGY_HINTS.get(strategy, "")

    messages = [
        {
            "role": "system",
            "content": PERSONA_PROMPT + strategy_hint
        }
    ]

    for msg in conversation_history[-6:]:
        role = "assistant" if msg["sender"] == "user" else "user"
        messages.append({
            "role": role,
            "content": msg["text"]
        })

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.8,
        max_tokens=80,
    )

    return response.choices[0].message.content.strip()
