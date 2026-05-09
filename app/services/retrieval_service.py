from app.services.vector_store_service import get_vector_store
from langsmith import traceable

@traceable(name="retrieve_documents")
def retrieve_documents(query:str):
    vector_store = get_vector_store()
    
    results =  vector_store.similarity_search_with_score(query=query, k=6)
    
    formatted_results = []
    
    for doc,score in results:
        formatted_results.append(
            {
            "content": doc.page_content,
            "metadata": doc.metadata,
            "score": score
            }
        )
        
    return formatted_results

    
