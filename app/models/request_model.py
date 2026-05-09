from pydantic import HttpUrl,BaseModel
from typing import List


class IngestRequest(BaseModel):
    urls: List[HttpUrl]
    

class SearchRequest(BaseModel):
    query: str
