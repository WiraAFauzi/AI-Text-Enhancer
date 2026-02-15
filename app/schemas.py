from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str
    mode: str

class TextResponse(BaseModel):
    result: str
    source: str
