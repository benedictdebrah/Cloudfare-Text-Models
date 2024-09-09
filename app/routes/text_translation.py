from fastapi import APIRouter
from app.models import TranslationRequest
from app.utils import translate_text

router = APIRouter(
    prefix="/translate",
    tags=["Translation"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def translate(translation_request: TranslationRequest):
    translation = translate_text(
        text=translation_request.text,
        source_lang=translation_request.source_lang,
        target_lang=translation_request.target_lang
    )
    return translation
