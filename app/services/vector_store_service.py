from langchain_qdrant import QdrantVectorStore

from app.db.qdrant import qdrant_client
from app.services.embedding_service import embedding_model
from app.core.config import settings


def get_vector_store():

    vector_store = QdrantVectorStore(
        client=qdrant_client,
        collection_name=settings.QDRANT_COLLECTION,
        embedding=embedding_model
    )

    return vector_store