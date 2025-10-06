"""
SQLite database connector for GenesisAgent persistent idea storage.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "genesis.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL;")
    return conn
