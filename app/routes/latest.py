from fastapi import APIRouter, Request  # , Form

# from app.core.auth import verify_api_key - not needed for latest it's public
from app.data.models import APIResponse, API_Error
from app.services.newz import get_latest
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
newz = get_latest()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", summary="Get the latest news", response_class=HTMLResponse)
def latest_newz(request: Request):
    if not newz:
        return API_Error(message="Latest news not available", code=404)
    latest = APIResponse(
        total=5,
        result=newz,
        status="success",
        code=200,
        message="Latest news fetched successfully",
    )

    # return latest
    return templates.TemplateResponse(
        "news.html", {"request": request, "items": latest.result}
    )
