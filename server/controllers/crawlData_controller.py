from fastapi import APIRouter
from services.crawlData_service import CrawlDataService
from models.Request.url_request_dto import UrlRequestDto

router = APIRouter(
    prefix="/crawl-data",
    tags=["Crawl-Data"]
)

@router.post("/")
async def importUrl(req: UrlRequestDto):
    data = CrawlDataService.getContextFromURL(req.url)
    return data