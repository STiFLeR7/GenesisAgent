"""
Persistence — SQLite I/O for idea storage.
"""

from .database import get_connection
from pathlib import Path

SCHEMA_PATH = Path(__file__).parent / "schema.sql"

def init_db():
    with get_connection() as conn, open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        conn.executescript(f.read())

def store_idea(content: str, score: float, agent_id: int, generation: int):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO ideas (content, score, agent_id, generation) VALUES (?,?,?,?)",
            (content, score, agent_id, generation),
        )
        conn.commit()

def fetch_top(limit: int = 10):
    with get_connection() as conn:
        return conn.execute(
            "SELECT content, score FROM ideas ORDER BY score DESC LIMIT ?", (limit,)
        ).fetchall()
