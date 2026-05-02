import sys
from db import (
    initialize_db,
    add_reminder,
    get_all_reminders,
    mark_reminder_done,
    get_today_reminders
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
Description: {r[2] if r[2] else "N/A"}
Due: {r[3] if r[3] else "N/A"}
Status: {r[4]}
Created: {r[5]}
------------------------
""")


def main():
    initialize_db()

    args = sys.argv

    if len(args) < 2:
        print("""
Usage:
  python3 app/main.py add "title"
  python3 app/main.py smart "text"
  python3 app/main.py list
  python3 app/main.py done <id>
  python3 app/main.py today
""")
        return

    command = args[1]

    if command == "add":
        title = args[2]
        add_reminder(title)
        print(f"Reminder added: {title}")

    elif command == "smart":
        user_input = args[2]
        parsed = parse_natural_input(user_input)

        add_reminder(
            parsed["title"],
            parsed["description"],
            parsed["due_date"]
        )

        print("AI parsed reminder:")
        print(parsed)

    elif command == "list":
        reminders = get_all_reminders()
        print_reminders(reminders)

    elif command == "done":
        reminder_id = int(args[2])
        mark_reminder_done(reminder_id)
        print(f"Reminder {reminder_id} marked as done")

    elif command == "today":
        reminders = get_today_reminders()

        print("\n=== TODAY'S SUMMARY ===\n")

        summary = generate_daily_summary(reminders)
        print(summary)

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()