import os
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def parse_natural_input(text):
    text_lower = text.lower()

    title = text
    due_date = None

    # RULE-BASED
    if "tomorrow" in text_lower:
        due = datetime.now() + timedelta(days=1)
        due_date = due.strftime("%Y-%m-%d")
        title = text_lower.replace("tomorrow", "").strip()

    elif "today" in text_lower:
        due = datetime.now()
        due_date = due.strftime("%Y-%m-%d")
        title = text_lower.replace("today", "").strip()

    # FALLBACK TO AI
    if due_date is None:
        return fallback_to_ai(text)

    return {
        "title": title.strip().capitalize(),
        "due_date": due_date,
        "description": None
    }

def fallback_to_ai(text):
    print("⚠️ Using AI fallback (OpenAI)")

    today = datetime.now().strftime("%Y-%m-%d")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"Today is {today}. "
                        "Extract reminder details from user input. "
                        "Return ONLY valid JSON with keys: "
                        "title, due_date (YYYY-MM-DD or null), description. "
                        "If relative date like 'next Monday' is mentioned, calculate it correctly."
                    )
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            temperature=0
        )

        output = response.choices[0].message.content.strip()

        parsed = json.loads(output)

        return {
            "title": parsed.get("title"),
            "due_date": parsed.get("due_date"),
            "description": parsed.get("description")
        }

    except Exception as e:
        print("AI parsing failed:", e)

        return {
            "title": text,
            "due_date": None,
            "description": None
        }


def generate_daily_summary(reminders):
    if not reminders:
        return "You have no tasks for today. Relax or plan something productive!"

    tasks = [r[1] for r in reminders]

    prompt = f"""
You are a productivity assistant.

Today's tasks:
{tasks}

Give a short summary:
- list tasks
- suggest priority
- give 1 productivity tip

Keep it concise.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return response.choices[0].message.content
