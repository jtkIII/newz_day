from pydantic import BaseModel
from typing import Any, List
from enum import Enum
from datetime import datetime


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


class CategoryEnum(str, Enum):
    technology = "technology"
    politics = "politics"
    culture = "culture"
    business = "business"
    programming = "programming"
    sports = "sports"
    entertainment = "entertainment"
    health = "health"
    science = "science"
    world = "world"
    finance = "finance"
    podcasts = "podcasts"
    education = "education"
    environment = "environment"
    lifestyle = "lifestyle"
    crypto = "crypto"
    privacy = "privacy"
    internet = "internet"
    gaming = "gaming"
    music = "music"


class NewsItem(BaseModel):
    id: int
    title: str
    timestamp: datetime  # was str; datetime is nicer for queries
    url: str
    summary: str
    source: str
    image_url: str | None = None
    category: CategoryEnum
