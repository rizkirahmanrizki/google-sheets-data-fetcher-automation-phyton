from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from config import SERVICE_ACCOUNT_INFO, SPREADSHEET_ID

creds = Credentials.from_service_account_info(SERVICE_ACCOUNT_INFO)
sheets_service = build("sheets", "v4", credentials=creds)

def get_token():
    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range="sessionToken!A1"
    ).execute()

    return result["values"][0][0]

def write_values(sheet_name, values):
    sheets_service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=f"{sheet_name}!A1",
        valueInputOption="USER_ENTERED",
        body={"values": values}
    ).execute()
