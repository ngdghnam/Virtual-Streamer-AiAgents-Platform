from fastapi import APIRouter
from models.Request.keywords_request_dto import KeywordRequestDto

router = APIRouter(
    prefix="/input-keyword",
    tags=["Keywords"]
)

@router.post("/")
async def inputKeywords(req: KeywordRequestDto):
    return {"kw": req.keyword}