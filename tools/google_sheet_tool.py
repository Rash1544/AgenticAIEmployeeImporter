import csv
import gspread
from google.oauth2.service_account import Credentials
from loguru import logger


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


def upload_to_google_sheet(csv_path):

    try:

        credentials = Credentials.from_service_account_file(
            "credentials/service_account.json",
            scopes=SCOPES,
        )

        client = gspread.authorize(credentials)

        spreadsheet = client.open("Agentic AI Employee Importer")

        sheet = spreadsheet.sheet1

        with open(csv_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            data = list(reader)

        sheet.clear()

        sheet.update(data)

        return spreadsheet.url

    except Exception as e:
        logger.error(f"Google Sheets Error: {e}")
        return None