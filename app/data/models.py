from pydantic import BaseModel
from typing import Any, List


class NetworkSummary(BaseModel):
    total_connections: int
    web_connections: int
    total_web_requests: int
    bots: dict


class APIResponse(BaseModel):
    total: int
    result: List[Any]
    status: str
    code: int
    message: str


class API_Error(BaseModel):
    message: str
    code: int
