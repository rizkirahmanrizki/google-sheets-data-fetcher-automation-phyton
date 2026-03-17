from config import DESIRED_COLS, CHAT_WEBHOOK_URL
from sheets import get_token, write_values
from metabase import fetch_metabase
from utils import compute_date_range, filter_columns
import requests

JOBS = [
    {
        "sheetName": "SF MAC",
        "endpoint": "/api/card/{cardId}/query/csv",
        "cardId": "XXXXX",
        "parameters": []
    }
]

def notify(msg):
    if CHAT_WEBHOOK_URL:
        requests.post(CHAT_WEBHOOK_URL, json={"text": msg})

def run():
    token = get_token()

    for job in JOBS:
        print(f"Running {job['sheetName']}")

        dr = compute_date_range()

        rows = fetch_metabase(
            job["endpoint"],
            job["cardId"],
            job["parameters"],
            token
        )

        header, body = rows[0], rows[1:]
        final = filter_columns(header, body, DESIRED_COLS)

        write_values(job["sheetName"], final)

        msg = f"{job['sheetName']} updated ({len(body)} rows)"
        print(msg)
        notify(msg)

if __name__ == "__main__":
    run()
