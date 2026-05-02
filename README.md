# 🧠 Personal Life Assistant

A lightweight AI-powered personal productivity assistant built in Python.

This project helps manage daily tasks, reminders, and recurring habits using a combination of rule-based logic and AI fallback parsing.

---

## 🚀 What it does (Current Features)

### ✅ Core Features
- Add and manage reminders via CLI
- Store tasks in SQLite database
- Mark tasks as done
- View all / pending / completed / upcoming tasks

### 🤖 AI Features
- Natural language task creation (e.g. "Pay rent next Monday")
- AI fallback parsing when rules are not enough
- Daily summary of tasks using AI

### 🔁 Automation
- Recurring tasks support:
  - daily
  - weekly
  - monthly

### 📊 Productivity Views
- Today’s tasks summary
- Pending tasks
- Completed tasks
- Upcoming tasks

---

## 🧰 Tech Stack

- Python 3
- SQLite (local database)
- OpenAI API (for optional AI parsing)
- CLI-based interface

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install openai python-dotenv