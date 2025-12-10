from pydantic import BaseModel
from typing import Any, List
from enum import Enum
from datetime import datetime
from datetime import timezone
from urllib.parse import urlparse
from urllib.parse import urlparse


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
    timestamp: datetime  # was str; datetime is nicer for queries (normalized to UTC)
    url: str
    summary: str
    source: str
    image_url: str | None = None
    category: CategoryEnum

    def __init__(self, **data):
        super().__init__(**data)
        ts = getattr(self, "timestamp", None)
        if ts is None:
            return
        # If naive, treat as UTC; if aware, convert to UTC
        if ts.tzinfo is None:
            self.timestamp = ts.replace(tzinfo=timezone.utc)
        else:
            self.timestamp = ts.astimezone(timezone.utc)

    @property
    def normalized_source(self) -> str:
        """Return a compact representation of the source URL:
        host (without leading www) optionally followed by the first path segment.
        Examples:
          https://www.example.com/section/article -> example.com/section
          https://news.site.org -> news.site.org
        """

        if not self.source:
            return ""
        try:
            p = urlparse(self.source)
            host = (p.netloc.split(":")[0] or "").lower()
            if host.startswith("www."):
                host = host[4:]
            first_seg = next((seg for seg in p.path.split("/") if seg), None)
            return f"{host}/{first_seg}" if first_seg else host
        except Exception:
            return self.source

    @property
    def dedupe_key(self) -> str:
        """A stable key used for deduplication that combines the parsed source
        host/first-segment and a normalized form of the item URL (host + path).
        """

        # normalize item URL: host (no www) + path (no trailing slash; "/" if empty)
        try:
            p = urlparse(self.url)
            host = (p.netloc.split(":")[0] or "").lower()
            if host.startswith("www."):
                host = host[4:]
            path = p.path.rstrip("/") or "/"
        except Exception:
            host = ""
            path = self.url or "/"

        src = self.normalized_source or ""
        return f"{src}|{host}{path}"
