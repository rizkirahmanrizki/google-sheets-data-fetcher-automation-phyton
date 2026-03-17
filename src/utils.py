from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

TIMEZONE = ZoneInfo("Asia/Jakarta")

def compute_date_range():
    now = datetime.now(TIMEZONE)
    monday = now - timedelta(days=now.weekday())
    monday = monday.replace(hour=0, minute=0, second=0, microsecond=0)

    return {
        "start": monday.strftime("%Y-%m-%d"),
        "end": (monday + timedelta(days=6)).strftime("%Y-%m-%d")
    }

def filter_columns(header, rows, desired_cols):
    indices = [header.index(c) if c in header else -1 for c in desired_cols]

    filtered = [
        [row[i] if i != -1 else "" for i in indices]
        for row in rows
    ]

    return [desired_cols] + filtered
