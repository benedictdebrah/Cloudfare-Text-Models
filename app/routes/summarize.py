from fastapi import APIRouter, Depends
from app.models import SummarizationRequest
from app.utils import summarize_text  
from typing import Dict
import os

router = APIRouter(
    prefix="/summarize",
    tags=["Summarization"],
    responses={404: {"description": "Not found"}},
)
def get_api_token():
    return os.getenv("API_TOKEN")

@router.post("/")
async def summarize(request: SummarizationRequest, api_token: str = Depends(get_api_token)) -> Dict:
    """
    Endpoint to summarize the input text.
    
    Parameters:
    - request: The request payload containing input_text and max_length.
    
    Returns:
    - The summarization result in JSON format.
    """
    result = summarize_text(api_token, request.input_text, request.max_length)
    return result