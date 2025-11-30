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
        image_url="https://images.unsplash.com/photo-1659084622165-6391a99e5ae8?w=800&q=80",
        category=CategoryEnum.technology,
    ),
    NewsItem(
        id=2,
        title="SpaceX achieves breakthrough",
        timestamp=datetime.now(timezone.utc),
        url="https://example.com/spacex",
        summary="Starship completes orbital flight.",
        source="Ars Technica",
        image_url="https://images.unsplash.com/photo-1444653614773-995cb1ef9efa?w=800&q=80",
        category=CategoryEnum.science,
    ),
    NewsItem(
        id=3,
        title="Global markets rally",
        timestamp=datetime.now(timezone.utc),
        url="https://example.com/markets",
        summary="Stocks soar amid economic optimism.",
        source="Bloomberg",
        image_url="https://images.unsplash.com/photo-1476242906366-d8eb64c2f661?w=800&q=80",
        category=CategoryEnum.finance,
    ),
    NewsItem(
        id=4,
        title="New advancements in renewable energy",
        timestamp=datetime.now(timezone.utc),
        url="https://example.com/renewable",
        summary="Solar and wind technologies improve efficiency.",
        source="Reuters",
        image_url="https://images.unsplash.com/photo-1509718443690-d8e2fb3474b7?w=800&q=80",
        category=CategoryEnum.environment,
    ),
    NewsItem(
        id=5,
        title="Breakthrough in cancer research",
        timestamp=datetime.now(timezone.utc),
        url="https://example.com/cancer-research",
        summary="New treatment shows promising results.",
        source="Medical News Today",
        image_url="https://images.unsplash.com/photo-1757159623175-c94243f0f2da?w=800&q=80",
        category=CategoryEnum.health,
    ),
    NewsItem(
        id=6,
        title="Historic peace agreement signed",
        timestamp=datetime.now(timezone.utc),
        url="https://example.com/peace-agreement",
        summary="Nations come together to end conflict.",
        source="BBC News",
        image_url="https://images.unsplash.com/photo-1750210955902-ce0e71765fb1?w=800&q=80",
        category=CategoryEnum.world,
    ),
    NewsItem(
        id=7,
        title="Championship game ends in dramatic fashion",
        timestamp=datetime.now(timezone.utc),
        url="https://example.com/championship",
        summary="Underdog team clinches victory in final seconds.",
        source="ESPN",
        image_url="https://images.unsplash.com/photo-1471295253337-3ceaaedca402?w=800&q=80",
        category=CategoryEnum.sports,
    ),
    NewsItem(
        id=8,
        title="New culinary trends emerge",
        timestamp=datetime.now(timezone.utc),
        url="https://example.com/culinary-trends",
        summary="Chefs experiment with fusion cuisine.",
        source="Food Network",
        image_url="https://images.unsplash.com/photo-1530281700549-e82e7bf110d6?w=800&q=80",
        category=CategoryEnum.lifestyle,
    ),
    NewsItem(
        id=9,
        title="Breakthroughs in quantum computing",
        timestamp=datetime.now(timezone.utc),
        url="https://example.com/quantum-computing",
        summary="Quantum processors achieve new milestones.",
        source="Wired",
        image_url="https://plus.unsplash.com/premium_photo-1756383544401-6df15ec16a14?w=800&q=80",
        category=CategoryEnum.technology,
    ),
]

path = ingest_news(items)
print("Wrote test parquet:", path)
