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


def add_reminder(title, description=None, due_date=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO reminders (title, description, due_date, status, created_at)
    VALUES (?, ?, ?, ?, ?)
    """, (
        title,
        description,
        due_date,
        "pending",
        get_current_timestamp()
    ))

    conn.commit()
    conn.close()


def get_all_reminders():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reminders")
    rows = cursor.fetchall()

    conn.close()
    return rows


def mark_reminder_done(reminder_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE reminders
    SET status = 'done'
    WHERE id = ?
    """, (reminder_id,))

    conn.commit()
    conn.close()


def get_today_reminders():
    conn = get_connection()
    cursor = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
    SELECT * FROM reminders
    WHERE due_date = ? AND status = 'pending'
    """, (today,))

    rows = cursor.fetchall()

    conn.close()
    return rows