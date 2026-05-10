# AGENTS.md — Personal Life Assistant

## Purpose
AI-powered CLI assistant for managing tasks, reminders, and routines.

## Rule
- Do not break existing CLI commands.
- AI is only used for parsing and summaries.
- SQLite is the source of truth.
- Preserve backward compatibility for all supported commands.

## Supported Commands
- add "title" [today|tomorrow] [daily|weekly|monthly]
- smart "text"
- list
- done <id>
- delete <id>
- edit <id> "new title"
- today
- pending
- completed
- upcoming

## Architecture
- `app/main.py` is the CLI entry point and command router.
- `app/db.py` contains all SQLite database operations.
- `app/ai.py` handles natural language parsing and summary generation.

## Safety
- Do not modify `.env`.
- Do not touch `data.db`.
- Do not change the database schema unless explicitly requested.
- Prefer minimal, targeted code changes.
- Keep all SQL parameterized.
- Run syntax validation after code changes.