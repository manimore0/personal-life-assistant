import sys
from db import (
    initialize_db,
    add_reminder,
    get_all_reminders,
    mark_reminder_done,
    get_today_reminders,
    get_pending_reminders,
    get_done_reminders,
    get_upcoming_reminders
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
------------------------
""")


def main():
    initialize_db()
    args = sys.argv

    if len(args) < 2:
        print("""
Commands:
  add "title"
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

    if cmd == "add":
        add_reminder(args[2])
        print("Reminder added")

    elif cmd == "smart":
        parsed = parse_natural_input(args[2])
        add_reminder(parsed["title"], parsed["description"], parsed["due_date"])
        print(parsed)

    elif cmd == "list":
        print_reminders(get_all_reminders())

    elif cmd == "done":
        mark_reminder_done(int(args[2]))
        print("Marked done")

    elif cmd == "today":
        summary = generate_daily_summary(get_today_reminders())
        print(summary)

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