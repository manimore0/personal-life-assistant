from datetime import datetime, timedelta
import os

# OPTIONAL: only used later
# from openai import OpenAI

def parse_natural_input(text):
    text_lower = text.lower()

    title = text
    due_date = None

    # RULE-BASED PARSING

    if "tomorrow" in text_lower:
        due = datetime.now() + timedelta(days=1)
        due_date = due.strftime("%Y-%m-%d")
        title = text_lower.replace("tomorrow", "").strip()

    elif "today" in text_lower:
        due = datetime.now()
        due_date = due.strftime("%Y-%m-%d")
        title = text_lower.replace("today", "").strip()

    # IF RULES FAIL → FALLBACK
    if due_date is None:
        return fallback_to_ai(text)

    return {
        "title": title.strip().capitalize(),
        "due_date": due_date,
        "description": None
    }


def fallback_to_ai(text):
    """
    Placeholder for AI call (we'll plug OpenAI later)
    """
    print("⚠️ Using AI fallback (not implemented yet)")

    return {
        "title": text,
        "due_date": None,
        "description": None
    }