from pydantic import HttpUrl,BaseModel
from typing import List


class IngestRequest(BaseModel):
    urls: List[HttpUrl]
    
    