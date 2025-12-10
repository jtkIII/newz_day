# app/routes/more.py

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.services.newz import get_latest_news

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def more(request: Request, page: int = 1, page_size: int = 20):
    offset = page * page_size
    items = get_latest_news(limit=page_size, offset=offset)

    # Calculate next page for button
    next_page = page + 1 if len(items) == page_size else None

    return templates.TemplateResponse(
        "_news_items_fragment.html",
        {"request": request, "items": items, "next_page": next_page},
    )
