from langsmith import traceable

from app.services.vector_store_service import get_vector_store


@traceable(name="retrieve_documents")
def retrieve_documents(query: str, limit: int = 5):

    vector_store = get_vector_store()

    results = vector_store.similarity_search_with_score(
        query=query,
        k=limit
    )

    MIN_SCORE = 0.5

    formatted_results = []

    for document, score in results:

        if score < MIN_SCORE:
            continue

        formatted_results.append({
            "content": document.page_content,
            "metadata": document.metadata,
            "score": score
        })

    return formatted_results