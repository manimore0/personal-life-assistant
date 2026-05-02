import sqlite3
from datetime import datetime
from datetime import timedelta

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
        recurrence TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()

def get_current_timestamp():
    return datetime.now().isoformat()

def add_reminder(title, description=None, due_date=None, recurrence=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO reminders (title, description, due_date, status, recurrence, created_at)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        title,
        description,
        due_date,
        "pending",
        recurrence,
        get_current_timestamp()
    ))

    conn.commit()
    conn.close()

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


def get_all_reminders():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reminders")
    rows = cursor.fetchall()

    conn.close()
    return rows


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


def get_pending_reminders():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM reminders
    WHERE status = 'pending'
    ORDER BY due_date ASC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows


def get_done_reminders():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM reminders
    WHERE status = 'done'
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows


def get_upcoming_reminders():
    conn = get_connection()
    cursor = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
    SELECT * FROM reminders
    WHERE due_date > ? AND status = 'pending'
    ORDER BY due_date ASC
    """, (today,))

    rows = cursor.fetchall()
    conn.close()
    return rows

def handle_recurring_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
    SELECT id, title, due_date, recurrence
    FROM reminders
    WHERE due_date = ? AND recurrence IS NOT NULL
    """, (today,))

    tasks = cursor.fetchall()

    for task in tasks:
        _, title, due_date, recurrence = task

        due = datetime.strptime(due_date, "%Y-%m-%d")

        if recurrence == "daily":
            next_due = due + timedelta(days=1)
        elif recurrence == "weekly":
            next_due = due + timedelta(days=7)
        elif recurrence == "monthly":
            next_due = due + timedelta(days=30)
        else:
            continue

        next_due_str = next_due.strftime("%Y-%m-%d")

        # 🔥 CHECK IF ALREADY EXISTS
        cursor.execute("""
        SELECT COUNT(*)
        FROM reminders
        WHERE title = ? AND due_date = ?
        """, (title, next_due_str))

        exists = cursor.fetchone()[0]

        if exists == 0:
            cursor.execute("""
            INSERT INTO reminders (title, due_date, status, recurrence, created_at)
            VALUES (?, ?, 'pending', ?, ?)
            """, (
                title,
                next_due_str,
                recurrence,
                get_current_timestamp()
            ))

    conn.commit()
    conn.close()