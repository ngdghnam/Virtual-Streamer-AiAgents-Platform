from pydantic import BaseModel

class UrlRequestDto(BaseModel):
    url: str
