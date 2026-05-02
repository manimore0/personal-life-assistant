import sys
from datetime import datetime, timedelta

from db import (
    initialize_db,
    add_reminder,
    get_all_reminders,
    mark_reminder_done,
    get_today_reminders,
    get_pending_reminders,
    get_done_reminders,
    get_upcoming_reminders,
    handle_recurring_tasks
)

from ai import parse_natural_input, generate_daily_summary


def print_reminders(reminders):
    if not reminders:
        print("No reminders found.\n")
        return

    for r in reminders:
        print(f"""
ID: {r[0]}
Title: {r[1]}
Due: {r[3] if r[3] else "N/A"}
Status: {r[4]}
Recurrence: {r[5] if r[5] else "None"}
------------------------
""")


def parse_date_keyword(keyword):
    if keyword == "today":
        return datetime.now().strftime("%Y-%m-%d")
    elif keyword == "tomorrow":
        return (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    return None


def main():
    initialize_db()

    # 🔁 handle recurring tasks safely
    handle_recurring_tasks()

    args = sys.argv

    if len(args) < 2:
        print("""
Commands:
  add "title" [today|tomorrow] [daily|weekly|monthly]
  smart "text"
  list
  done <id>
  today
  pending
  completed
  upcoming
""")
        return

    cmd = args[1]

    # ---------------- ADD ----------------
    if cmd == "add":
        if len(args) < 3:
            print("Usage: add \"title\" [today|tomorrow] [recurrence]")
            return

        title = args[2]
        due_date = None
        recurrence = None

        if len(args) >= 4:
            maybe_date = args[3]
            parsed_date = parse_date_keyword(maybe_date)

            if parsed_date:
                due_date = parsed_date
            else:
                recurrence = maybe_date

        if len(args) == 5:
            recurrence = args[4]

        add_reminder(
            title,
            description=None,
            due_date=due_date,
            recurrence=recurrence
        )

        print(f"Reminder added: {title}, due={due_date}, recurrence={recurrence}")

    # ---------------- SMART ----------------
    elif cmd == "smart":
        if len(args) < 3:
            print("Usage: smart \"text\"")
            return

        user_input = args[2]
        parsed = parse_natural_input(user_input)

        add_reminder(
            parsed["title"],
            parsed["description"],
            parsed["due_date"]
        )

        print("\nAI parsed reminder:")
        print(parsed)

    # ---------------- LIST ----------------
    elif cmd == "list":
        print_reminders(get_all_reminders())

    # ---------------- DONE ----------------
    elif cmd == "done":
        if len(args) < 3:
            print("Usage: done <id>")
            return

        reminder_id = int(args[2])
        mark_reminder_done(reminder_id)
        print(f"Reminder {reminder_id} marked as done")

    # ---------------- TODAY SUMMARY ----------------
    elif cmd == "today":
        reminders = get_today_reminders()

        print("\n=== TODAY'S SUMMARY ===\n")
        summary = generate_daily_summary(reminders)
        print(summary)

    # ---------------- FILTERS ----------------
    elif cmd == "pending":
        print_reminders(get_pending_reminders())

    elif cmd == "completed":
        print_reminders(get_done_reminders())

    elif cmd == "upcoming":
        print_reminders(get_upcoming_reminders())

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()