import sys
from pathlib import Path

# Add project root to PYTHONPATH so "import app" works
ROOT = Path(__file__).resolve().parents[1]  # adjust if scripts/ is one level deep
sys.path.insert(0, str(ROOT))

from datetime import datetime, timezone  # noqa: E402
from app.data.models import NewsItem, CategoryEnum  # noqa: E402
from app.services.ingest import ingest_news  # noqa: E402

items = [
    NewsItem(
        id=1,
        title="OpenAI launches new model",
        timestamp=datetime.now(timezone.utc),
        url="https://example.com/ai",
        summary="A powerful new model is announced.",
        source="TechCrunch",
        image_url="https://placehold.co/600x400",
        category=CategoryEnum.technology,
    ),
    NewsItem(
        id=2,
        title="SpaceX achieves breakthrough",
        timestamp=datetime.now(timezone.utc),
        url="https://example.com/spacex",
        summary="Starship completes orbital flight.",
        source="Ars Technica",
        image_url="https://placehold.co/600x400",
        category=CategoryEnum.science,
    ),
    NewsItem(
        id=3,
        title="Global markets rally",
        timestamp=datetime.now(timezone.utc),
        url="https://example.com/markets",
        summary="Stocks soar amid economic optimism.",
        source="Bloomberg",
        image_url="https://placehold.co/600x400",
        category=CategoryEnum.finance,
    ),
    NewsItem(
        id=4,
        title="New advancements in renewable energy",
        timestamp=datetime.now(timezone.utc),
        url="https://example.com/renewable",
        summary="Solar and wind technologies improve efficiency.",
        source="Reuters",
        image_url="https://placehold.co/600x400",
        category=CategoryEnum.environment,
    ),
    NewsItem(
        id=5,
        title="Breakthrough in cancer research",
        timestamp=datetime.now(timezone.utc),
        url="https://example.com/cancer-research",
        summary="New treatment shows promising results.",
        source="Medical News Today",
        image_url="https://placehold.co/600x400",
        category=CategoryEnum.health,
    ),
]

path = ingest_news(items)
print("Wrote test parquet:", path)
