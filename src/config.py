import os
from dotenv import load_dotenv

load_dotenv()

SERVICE_ACCOUNT_INFO = {
    "type": "service_account",
    "project_id": os.getenv("GCP_PROJECT_ID"),
    "private_key_id": os.getenv("GCP_PRIVATE_KEY_ID"),
    "private_key": os.getenv("GCP_PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": os.getenv("GCP_CLIENT_EMAIL"),
    "client_id": os.getenv("GCP_CLIENT_ID"),
    "token_uri": "https://oauth2.googleapis.com/token",
}

MB_BASE_URL = os.getenv("MB_BASE_URL")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
TOKEN_SHEET_ID = os.getenv("TOKEN_SHEET_ID")
CHAT_WEBHOOK_URL = os.getenv("CHAT_WEBHOOK_URL")

DESIRED_COLS = [
    "shipment_id","shipment_type","order_id","bulky_flag","offload_flag",
    "b2br_flag","prior_tag","shipment_orig_hub_name","shipment_dest_hub_name",
    "poa_datetime","close_shipment_datetime","crossdock_van_inbound_datetime","wave_ref"
]
