# 🧠 Personal Life Assistant

A lightweight AI-powered personal productivity assistant built in Python.

This project helps manage daily tasks, reminders, and recurring habits using a combination of rule-based logic and AI fallback parsing.

---

## 🚀 What it does (Current Features)

### ✅ Core Features
- Add and manage reminders via CLI
- Store tasks in SQLite database
- Edit existing reminder titles
- Mark tasks as done
- Delete reminders
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
```

### 2. Run the application

```bash
python3 app/main.py
```

---

## 💻 Available Commands

```bash
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

## 🗄️ Data Storage

All reminders are stored locally in:

```text
data.db
```

The main table contains:
- id
- title
- description
- due_date
- status
- recurrence
- created_at

---

## 🎯 Project Goal

Build a personal AI assistant that helps manage:
- Tasks
- Reminders
- Habits
- Daily planning
- Productivity workflows

---

## 🚀 Future Enhancements

- Voice command support
- Calendar integration
- Notifications
- Web dashboard
- Mobile app
- Habit streak tracking