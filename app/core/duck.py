import duckdb
from pathlib import Path
from threading import Lock

# Path to your persistent metadata DB
DB_PATH = Path("app/db/metadata.duckdb")

# Global lock to prevent concurrent write attempts
_duck_lock = Lock()

# Cached connection (DuckDB embeds itself; safe in many cases)
_con = None


def get_con():
    """
    Returns a singleton DuckDB connection.
    DuckDB runs in-process so we avoid recreating connections constantly.
    """
    global _con
    if _con is None:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        _con = duckdb.connect(str(DB_PATH))
        _init_db(_con)
    return _con


def _init_db(con):
    """
    Create metadata tables if they do not exist.
    This runs once on first connection.
    """
    con.execute("""
        CREATE TABLE IF NOT EXISTS article_hashes (
            hash TEXT PRIMARY KEY,
            first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    con.execute("""
        CREATE TABLE IF NOT EXISTS summaries (
            id TEXT PRIMARY KEY,
            summary TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)


def query_df(sql: str, *params):
    """
    Runs a read-only query and returns a Pandas DataFrame.
    Uses the shared connection.
    """
    con = get_con()
    return con.execute(sql, params).fetchdf()


def query_one(sql: str, *params):
    """
    Returns a single row as a tuple or None.
    """
    con = get_con()
    result = con.execute(sql, params).fetchone()
    return result


def execute(sql: str, *params):
    """
    Executes a write statement safely (INSERT, UPDATE, DELETE).
    Uses a lock to prevent concurrent writes from colliding.
    """
    con = get_con()
    with _duck_lock:
        return con.execute(sql, params)
