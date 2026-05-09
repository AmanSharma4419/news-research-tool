from langchain_openai import OpenAI
from app.core.config import settings

llm = OpenAI(
    model="gpt-4o-mini",
    api_key=settings.OPENAI_API_KEY,
    temperature=0
)