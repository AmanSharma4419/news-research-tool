from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    QDRANT_URL: str
    QDRANT_COLLECTION: str

    class Config:
        env_file = ".env",
        extra="ignore"



settings = Settings()