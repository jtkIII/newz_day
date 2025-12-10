from fastapi import APIRouter, Depends

from app.core.auth import verify_api_key
from app.data.models import APIResponse, API_Error
from app.services.newz import get_hottest

router = APIRouter()

# router = APIRouter(dependencies=[Depends(verify_api_key)])
newz = get_hottest()


@router.get("/", summary="Get the hottest news", response_model=APIResponse | API_Error)
def hottest_newz():
    if not newz:
        return API_Error(message="Hottest news not available", code=404)
    hottest = APIResponse(
        total=5,
        result=newz,
        status="success",
        code=200,
        message="Hottest news fetched successfully",
    )

    return hottest
