from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from decouple import config


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = config("SHEET_ID")

try:
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    bodyValue = [["25/04/2022", "192.168.0.15"]]

    request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="IpHist!A:B",
                                    valueInputOption="USER_ENTERED",
                                    body={"values": bodyValue}).execute()

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="IpHist!A1:B1").execute()
    values = result.get('values', [])

    print(values)

except HttpError as err:
    print(err)
  