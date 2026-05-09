from langsmith import traceable

from app.services.retrieval_service import retrieve_documents
from app.services.llm_service import llm
from app.prompts.rag_prompt import RAG_PROMPT


@traceable(name="rag_pipeline")
def ask_question(question: str):

    retrieved_docs = retrieve_documents(question)

    context = "\n\n".join(
        [doc["content"] for doc in retrieved_docs]
    )

    final_prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    response = llm.invoke(final_prompt)

    sources = []

    for doc in retrieved_docs:

        sources.append({
            "title": doc["metadata"].get("title"),
            "source_url": doc["metadata"].get("source_url")
        })

    return {
        "question": question,
        "answer": response,
        "sources": sources
    }