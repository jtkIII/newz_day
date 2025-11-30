# app/routes/latest.py
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.services.newz import get_latest_news

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", summary="Get the latest news", response_class=HTMLResponse)
def latest_news(request: Request):
    items = get_latest_news(limit=20)

    return templates.TemplateResponse("news.html", {"request": request, "items": items})
