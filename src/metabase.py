import requests, csv, io
from config import MB_BASE_URL

def fetch_metabase(endpoint, card_id, parameters, token):
    url = MB_BASE_URL + endpoint.replace("{cardId}", card_id)

    data = "parameters=" + requests.utils.quote(str(parameters).replace("'", '"'))

    resp = requests.post(
        url,
        data=data,
        headers={
            "X-Metabase-Session": token,
            "Content-Type": "application/x-www-form-urlencoded"
        }
    )

    if not resp.ok:
        raise RuntimeError(f"{resp.status_code}: {resp.text[:200]}")

    reader = csv.reader(io.StringIO(resp.text))
    return list(reader)
