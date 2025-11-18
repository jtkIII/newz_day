from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

from app.routes import hottest, latest, summary
from app.core.config import settings
from app.services import netstats


@asynccontextmanager  # Lifespan context replaces deprecated on_event
async def lifespan(app: FastAPI):
    # Startup
    if settings.debug:
        print("newz.day API started in DEBUG mode")
        print(f"API key loaded? {'yes' if settings.api_key else 'no'}")
        if settings.allowed_ips:
            print(f"Allowed IPs: {settings.allowed_ips}")

    yield  # run the app

    # Shutdown
    if settings.debug:
        print("Shutting down Network Monitor API")


app = FastAPI(title="Newz.day API", version="1.0", lifespan=lifespan)


@app.middleware("http")
async def request_middleware(request: Request, call_next):
    if request.client is None:
        ip = "unknown"
    else:
        ip = request.client.host
    ua = request.headers.get("user-agent", "")
    path = request.url.path
    netstats.log_request(ip, ua, path)
    response = await call_next(request)
    return response


app.include_router(hottest.router, prefix="/api/v1/hottest", tags=["hottest"])
app.include_router(latest.router, prefix="/api/v1/latest", tags=["latest"])
app.include_router(summary.router, prefix="/api/v1/summary", tags=["summary"])


@app.get(
    "/",
    summary="Newz.Day",
    description="Newz.Day API status, endpoints, and debug status.",
)
async def root():
    return {
        "message": "Newz.Day",
        "version": app.version,
        "debug": settings.debug,
        "hottest_endpoint": "/api/v1/hottest/",
        "latest_endpoint": "/api/v1/latest/",
        "summary_endpoint": "/api/v1/summary/",
    }
