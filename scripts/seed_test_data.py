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
        id=11,
        title="Hoddogs AI model released",
        timestamp=datetime.now(timezone.utc),
        url="https://techcrunch.com/ai",
        summary="A powerful new model is announced.",
        source="TechCrunch",
        image_url="https://images.unsplash.com/photo-1757904257493-cc04d1dc2691?w=800&q=80",
        category=CategoryEnum.technology,
    ),
    NewsItem(
        id=12,
        title="Looks like Starship finally flew",
        timestamp=datetime.now(timezone.utc),
        url="https://spacex.com/starship",
        summary="Starship completes orbital flight.",
        source="Ars Technica",
        image_url="https://images.unsplash.com/photo-1707767633536-2d6614bf2865?w=800&q=80",
        category=CategoryEnum.science,
    ),
    NewsItem(
        id=13,
        title="Dem Dim Sums rally the markets",
        timestamp=datetime.now(timezone.utc),
        url="https://foxnews.com/markets",
        summary="Stocks soar amid economic optimism.",
        source="Bloomberg",
        image_url="https://images.unsplash.com/photo-1697365434888-796136cf2796?w=800&q=80",
        category=CategoryEnum.finance,
    ),
    NewsItem(
        id=14,
        title="Old School Gamers embrace retro consoles",
        timestamp=datetime.now(timezone.utc),
        url="https://cnn.com/renewable",
        summary="Solar and wind technologies improve efficiency.",
        source="Reuters",
        image_url="https://images.unsplash.com/photo-1757444838044-d9dcb1bb3017?w=800&q=80",
        category=CategoryEnum.environment,
    ),
    NewsItem(
        id=15,
        title="The Doorway to the unknown",
        timestamp=datetime.now(timezone.utc),
        url="https://nothenews.com/cancer-research",
        summary="New tenements shows promising results.",
        source="Medical News Today",
        image_url="https://images.unsplash.com/photo-1754079132889-ac902392494e?w=800&q=80",
        category=CategoryEnum.health,
    ),
    NewsItem(
        id=16,
        title="Historic house goes wild",
        timestamp=datetime.now(timezone.utc),
        url="https://headlin3s.com/peace-agreement",
        summary="Nations come together to end conflict.",
        source="BBC News",
        image_url="https://images.unsplash.com/photo-1750210955902-ce0e71765fb1?w=800&q=80",
        category=CategoryEnum.world,
    ),
    NewsItem(
        id=17,
        title="Championship game ends in dramatic fashion",
        timestamp=datetime.now(timezone.utc),
        url="https://espn.com/championship",
        summary="Underdog team clinches victory in final seconds.",
        source="ESPN",
        image_url="https://images.unsplash.com/photo-1485400031595-976c74cf4e25?w=800&q=80",
        category=CategoryEnum.sports,
    ),
    NewsItem(
        id=18,
        title="New culinary trends emerge",
        timestamp=datetime.now(timezone.utc),
        url="https://example.com/culinary-trends",
        summary="Chefs experiment with fusion cuisine.",
        source="Food Network",
        image_url="https://images.unsplash.com/photo-1530281700549-e82e7bf110d6?w=800&q=80",
        category=CategoryEnum.lifestyle,
    ),
    NewsItem(
        id=19,
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
