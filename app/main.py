from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.qdrant import qdrant_client
from app.api.routes.ingest import router as ingest_router
from app.db.qdrant_setup import create_collection


@asynccontextmanager
async def lifespan(app: FastAPI):

    create_collection()

    yield

    print("Application shutting down")


app = FastAPI(
    title="AI News Research Tool",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/health")
async def health_check():

    return {
        "status": "healthy",
        "service": "news-research-tool"
    }


@app.get("/qdb-status")
async def qdb_status():

    collections = qdrant_client.get_collections()

    return {
        "qdrant_status": "connected",
        "collections": collections.dict()
    }


app.include_router(ingest_router)