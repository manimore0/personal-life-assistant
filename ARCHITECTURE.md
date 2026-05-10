# 🏗 Architecture — Personal Life Assistant

This document explains how the system is structured and how data flows through the application.

---

## 🔄 High-Level Flow

```text
CLI (main.py)
     ↓
Command Router
     ↓
Rule-based logic (fast path)
     ↓ (if needed)
AI Parser (fallback)
     ↓
SQLite Database (data layer)
     ↓
Recurring Engine
     ↓
Filter + Summary Layer
```

---

## 📁 Core Modules

### `app/main.py`
CLI entry point and command router.

Responsibilities:
- Parse command-line arguments
- Route commands to database and AI functions
- Display reminders and summaries

### `app/db.py`
SQLite data access layer.

Responsibilities:
- Initialize database schema
- Insert reminders
- Update reminder titles
- Delete reminders
- Mark reminders as done
- Query reminders by status/date
- Generate recurring tasks

### `app/ai.py`
AI integration layer.

Responsibilities:
- Parse natural language into structured reminder fields
- Generate daily summaries from today's tasks

---

## 💻 Supported CLI Commands

```text
add "title" [today|tomorrow] [daily|weekly|monthly]
smart "text"
list
done <id>
delete <id>
edit <id> "new title"
today
pending
completed
upcoming
```

---

## 🗄️ Database Schema

### `reminders`

| Column      | Type    | Description |
|-----------|---------|-------------|
| id        | INTEGER | Primary key |
| title     | TEXT    | Reminder title |
| description | TEXT  | Optional notes |
| due_date  | TEXT    | YYYY-MM-DD |
| status    | TEXT    | pending / done |
| recurrence | TEXT   | daily / weekly / monthly |
| created_at | TEXT   | Creation timestamp |

---

## 🔁 Recurring Task Engine

At application startup, `handle_recurring_tasks()` checks for recurring reminders due today and creates the next occurrence.

Supported recurrence types:
- daily
- weekly
- monthly

---

## 🤖 AI Layer

The AI module is used only when:
- The `smart` command is invoked
- The `today` summary is generated

This keeps the core system deterministic and fast while using AI as an enhancement layer.