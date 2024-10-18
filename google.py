def gogle(g):
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd

# Ielādē akreditācijas failu un nosaka vajadzīgo API darbības loku
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'

# Izveido servisu, lai piekļūtu Google Sheets
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Definē Google Sheets ID un lapas nosaukumu, kur glabājas veidlapas atbildes
SPREADSHEET_ID = 'your_google_sheets_id'
RANGE_NAME = 'Form Responses 1'  # Noklusētais nosaukums

# Izveido servisu, lai nolasītu Sheets datus
service = build('sheets', 'v4', credentials=creds)

# Izsauc API, lai iegūtu tabulas saturu
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range=RANGE_NAME).execute()

# Iegūst atbildes
values = result.get('values', [])

# Pārveido par DataFrame, ja vēlies to izmantot ar pandas
if not values:
    print('No data found.')
else:
    df = pd.DataFrame(values[1:], columns=values[0])
    print(df)
gogle()
