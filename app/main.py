from db import (
    initialize_db,
    get_all_reminders,
    mark_reminder_done
)


def main():
    initialize_db()

    print("\n=== PERSONAL LIFE ASSISTANT ===\n")

    reminders = get_all_reminders()

    if not reminders:
        print("No reminders found.\n")
        return

    print("All reminders:\n")

    for r in reminders:
        print(f"""
ID: {r[0]}
Title: {r[1]}
Description: {r[2]}
Due: {r[3]}
Status: {r[4]}
Created: {r[5]}
------------------------
""")

    # TEMP TEST: mark first reminder as done
    print("\nMarking first reminder as done...\n")
    mark_reminder_done(reminders[0][0])


if __name__ == "__main__":
    main()