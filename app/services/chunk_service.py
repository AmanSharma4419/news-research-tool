from langchain_text_splitters import RecursiveCharacterTextSplitter
from langsmith import traceable

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
    )

@traceable(name="text_chunking")
def text_splitting(text:str):
    chunks = text_splitter.split_text(text)
    return chunks