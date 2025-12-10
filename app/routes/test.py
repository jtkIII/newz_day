import time
import json
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

# Try FastAPI
try:
    router = APIRouter()

    @router.get("/test")
    async def test_route(request: Request, msg: str = "hello"):
        """FastAPI test route: GET /test?msg=..."""
        return JSONResponse(
            {
                "ok": True,
                "framework": "fastapi",
                "msg": msg,
                "path": str(request.url.path),
                "ts": time.time(),
            }
        )

except Exception:
    router = None
