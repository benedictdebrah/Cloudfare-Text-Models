from fastapi import FastAPI
from app.routes import chat, summarize, text_translation

app = FastAPI()

app.include_router(chat.router)
app.include_router(summarize.router)
app.include_router(text_translation.router)
