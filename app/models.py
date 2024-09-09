from pydantic import BaseModel
from typing import Union

class RequestModel(BaseModel):
    prompt: str
    


class SummarizationRequest(BaseModel):
    input_text: str
    max_length: int



class TranslationRequest(BaseModel):
    text: str
    source_lang: str
    target_lang: str