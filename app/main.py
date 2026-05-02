import sys
from db import (
    initialize_db,
    add_reminder,
    get_all_reminders,
    mark_reminder_done
)


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
  python3 app/main.py add "title" "description(optional)" "due_date(optional)"
  python3 app/main.py list
  python3 app/main.py done <id>
""")
        return

    command = args[1]

    # ADD REMINDER
    if command == "add":
        if len(args) < 3:
            print("Please provide a title")
            return

        title = args[2]
        description = args[3] if len(args) > 3 else None
        due_date = args[4] if len(args) > 4 else None

        add_reminder(title, description, due_date)
        print(f"Reminder added: {title}")

    # LIST REMINDERS
    elif command == "list":
        reminders = get_all_reminders()
        print_reminders(reminders)

    # MARK DONE
    elif command == "done":
        if len(args) < 3:
            print("Please provide reminder ID")
            return

        try:
            reminder_id = int(args[2])
            mark_reminder_done(reminder_id)
            print(f"Reminder {reminder_id} marked as done")
        except ValueError:
            print("Invalid ID. Please enter a number.")

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()