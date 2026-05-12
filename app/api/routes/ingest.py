from fastapi import APIRouter

from app.models.request_model import IngestRequest
from app.services.ingestion_service import ingest_urls


router = APIRouter()

@router.post("/ingest")
async def ingest_data(payload:IngestRequest):
        result = ingest_urls(payload.urls)
        return result