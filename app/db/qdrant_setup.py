from qdrant_client.models import Distance, VectorParams

from app.db.qdrant import qdrant_client
from app.core.config import settings


def create_collection():

    collections = qdrant_client.get_collections().collections

    collection_names = [
        collection.name
        for collection in collections
    ]

    if settings.QDRANT_COLLECTION not in collection_names:

        qdrant_client.create_collection(
            collection_name=settings.QDRANT_COLLECTION,

            vectors_config=VectorParams(
                size=1536,
                distance=Distance.COSINE
            )
        )

        print("Qdrant collection created")

    else:
        print("Collection already exists")