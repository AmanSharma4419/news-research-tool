from fastapi import APIRouter

from app.services.rag_service import ask_question

router = APIRouter()

@router.get("/ask")
async def ask(query: str):

    result = ask_question(query)

    return result