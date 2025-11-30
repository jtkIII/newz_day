from pathlib import Path
from datetime import datetime, timezone
import uuid
import pandas as pd

from app.data.models import NewsItem

DATA_DIR = Path("data/raw")


def ingest_news(items: list[NewsItem]) -> Path:
    """
    Takes a list of NewsItem objects and writes them to a date-partitioned
    Parquet file for later DuckDB querying.

    Returns the full path to the written parquet file.
    """

    if not items:
        raise ValueError("ingest_news() received an empty list")

    # Convert List[NewsItem] -> List[dict]
    rows = [item.model_dump() for item in items]

    df = pd.DataFrame(rows)

    # Ensure output directories exist
    now = datetime.now(timezone.utc)
    year = str(now.year)
    month = f"{now.month:02d}"
    day = f"{now.day:02d}"

    folder = DATA_DIR / year / month / day
    folder.mkdir(parents=True, exist_ok=True)

    # Filename pattern: batch_YYYYMMDD_HHMMSS_UUID.parquet
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    filename = f"batch_{timestamp}_{uuid.uuid4().hex[:8]}.parquet"

    filepath = folder / filename

    # Write parquet
    df.to_parquet(filepath, index=False)
    # df.to_parquet("data/raw/latest_batch.parquet", engine="pyarrow", index=False)

    return filepath
