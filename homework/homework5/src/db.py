# src/db.py
from __future__ import annotations
import sqlite3
from pathlib import Path

DB_PATH = Path("data") / "bootcamp_stage5.db"

def get_connection(db_path: str | Path = DB_PATH) -> sqlite3.Connection:
   
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")  # good practice
    return conn

def init_db(conn: sqlite3.Connection) -> None:
    """
    Creates a simple table for our exercises.
    We'll store daily revenue and a toy 'risk_score'.
    """
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,         -- ISO date like '2025-08-17'
            revenue REAL NOT NULL,      -- example numeric
            risk_score REAL NOT NULL    -- example numeric
        );

        -- an index for faster lookups by date
        CREATE INDEX IF NOT EXISTS idx_metrics_date ON metrics(date);
        """
    )
    conn.commit()

def insert_sample_rows(conn: sqlite3.Connection) -> None:
    """
    Inserts a few rows so we can test reads/writes immediately.
    Safe to re-run; it won't duplicate the exact same dates.
    """
    # upsert-ish behavior using INSERT OR IGNORE via a unique constraint is ideal,
    # but to keep it simple we’ll just check first.
    existing_dates = {row[0] for row in conn.execute("SELECT date FROM metrics")}
    rows = [
        ("2025-08-14", 1200.0, 0.35),
        ("2025-08-15", 1525.0, 0.30),
        ("2025-08-16", 980.0,  0.55),
        ("2025-08-17", 1730.0, 0.28),
    ]
    to_insert = [r for r in rows if r[0] not in existing_dates]
    if to_insert:
        conn.executemany(
            "INSERT INTO metrics (date, revenue, risk_score) VALUES (?, ?, ?)",
            to_insert
        )
        conn.commit()
