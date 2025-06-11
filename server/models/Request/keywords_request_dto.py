from pydantic import BaseModel

class KeywordRequestDto(BaseModel):
    keyword: str
