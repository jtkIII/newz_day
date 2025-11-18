from fastapi import APIRouter, Depends

from app.core.auth import verify_api_key
from app.data.models import APIResponse, API_Error
from app.services.newz import get_latest

router = APIRouter(dependencies=[Depends(verify_api_key)])
newz = get_latest()


@router.get("/", summary="Get the latest news", response_model=APIResponse | API_Error)
def latest_newz():
    if not newz:
        return API_Error(message="Latest news not available", code=404)
    latest = APIResponse(
        total=5,
        result=newz,
        status="success",
        code=200,
        message="Latest news fetched successfully",
    )

    return latest
