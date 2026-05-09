from fastapi import APIRouter

from app.models.request_model import SearchRequest

from app.services.retrieval_service import retrieve_documents


router = APIRouter()


@router.get("/search")
async def retrieve_data(payload:SearchRequest):
        result = retrieve_documents(payload.query)
        print(result,"result")
        return result