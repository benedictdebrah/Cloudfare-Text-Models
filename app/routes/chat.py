from fastapi import APIRouter
from ..utils import fingertips_ai_interaction

router = APIRouter(
    prefix="/fingertips",
    tags=["FingertipsAI"],
    responses={404: {"description": "Not found"}},
)


@router.post("/chat")
async def fingertips_chat(prompt: str):
    response = fingertips_ai_interaction(prompt)
    return response