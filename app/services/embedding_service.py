from langchain_openai import OpenAIEmbeddings
from app.core.config import BaseSettings

embedding_model = OpenAIEmbeddings(
    api_key=BaseSettings.OPENAI_API_KEY,
    model="text-embedding-3-small"
)