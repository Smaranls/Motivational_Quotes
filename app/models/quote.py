from pydantic import BaseModel

class Quote(BaseModel):
    author: str
    quote: str
