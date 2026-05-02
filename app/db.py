import sqlite3
from datetime import datetime

DB_NAME = "data.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT,
        status TEXT DEFAULT 'pending',
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


def get_current_timestamp():
    return datetime.now().isoformat()