from fastapi import APIRouter, Header, HTTPException
from app.models.schemas import HoneyPotRequest, HoneyPotResponse
from app.services.conversation_manager import process_message
from app.config import settings

router = APIRouter()


@router.post("/honeypot", response_model=HoneyPotResponse)
def honeypot_endpoint(
    request: HoneyPotRequest,
    x_api_key: str = Header(...)
):
    # -------- API Key Validation --------
    if x_api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # -------- Process Message --------
    response = process_message(request.dict())

    return response
