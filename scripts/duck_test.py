import sys
from pathlib import Path

# Add project root to PYTHONPATH so "import app" works
ROOT = Path(__file__).resolve().parents[1]  # adjust if scripts/ is one level deep
sys.path.insert(0, str(ROOT))
from app.core.duck import query_df

df = query_df("""
    SELECT *
    FROM 'data/raw/**/*.parquet'
    ORDER BY timestamp DESC
    LIMIT 10
""")

print(df)
