import sys
from pathlib import Path

# Add project root to PYTHONPATH so "import app" works
ROOT = Path(__file__).resolve().parents[1]  # adjust if scripts/ is one level deep
sys.path.insert(0, str(ROOT))
from typing import List
from app.data.models import NewsItem, CategoryEnum
import pandas as pd
from app.core.duck import query_df


def query_latest_news(limit: int = 20) -> List[NewsItem]:
    df = query_df(f"""
        SELECT *
        FROM 'data/raw/**/*.parquet'
        ORDER BY timestamp DESC
        LIMIT {limit}
    """)
    return [NewsItem(**row) for row in df.to_dict(orient="records")]  # type: ignore


if __name__ == "__main__":
    latest_news = query_latest_news()
    for item in latest_news:
        print(f"{item.timestamp} - {item.title} ({item.source})")
