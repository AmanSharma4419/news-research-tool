from fastapi import FastAPI
from app.db.qdrant import qdrant_client

app = FastAPI(
    title="AI News Research Tool",
    version="1.0.0"
)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "news-research-tool"
    }
    
@app.get("/qdb-status")
async def home():

    collections = qdrant_client.get_collections()

    return {
        "qdrant_status": "connected",
        "collections": collections.dict()
    }