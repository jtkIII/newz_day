# app/routes/summary.py
from fastapi import APIRouter, Depends

from app.core.auth import verify_api_key
from app.data.models import APIResponse, API_Error
from app.services.newz import get_latest, get_hottest

router = APIRouter(dependencies=[Depends(verify_api_key)])

latest = get_latest()
hottest = get_hottest()
newz = [
    {"latest": latest},
    {"hottest": hottest},
]


@router.get("/", summary="Get news summary", response_model=APIResponse | API_Error)
def newz_summary():
    if not newz:
        return API_Error(message="News Summary not available", code=404)
    summary = APIResponse(
        total=5,
        result=newz,
        status="success",
        code=200,
        message="Summary news fetched successfully",
    )
    return summary
