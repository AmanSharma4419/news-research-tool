from langchain_core.documents import Document

from app.services.loader_service import load_article
from app.services.chunk_service import text_splitting
from app.services.vector_store_service import get_vector_store
from langsmith import traceable

@traceable(name="ingest_urls_pipeline")
def ingest_urls(urls: list):

    documents = []

    for url in urls:

        print(f"Processing URL: {url}")

        article_data = load_article(str(url))

        chunks = text_splitting(article_data["content"])

        print(f"Chunks created: {len(chunks)}")

        for index, chunk in enumerate(chunks):

            document = Document(
                page_content=chunk,
                metadata={
                    "title": article_data["title"],
                    "source_url": article_data["source_url"],
                    "chunk_index": index
                }
            )

            documents.append(document)

        print(f"Successfully processed: {url}")

    vector_store = get_vector_store()

    vector_store.add_documents(documents)

    return {
        "status": "success",
        "documents_inserted": len(documents)
    }