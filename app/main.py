from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Agentic HoneyPot API",
    description="Detects scam messages, engages scammers, extracts intelligence, and reports to GUVI.",
    version="1.0.0"
)

app.include_router(router)
