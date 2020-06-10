from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
MICROGREENS_SPREADSHEET_ID = '18z6wp-rFMI5s_XQ4d2yhzR0HTwvO-lnq7z4u714qpgI'
CONTACT_RANGE = 'Contact!A1:I30'
HARVEST_OFFSET = 'harvest_offset!A1:G3'

def read_harvest_offset(sheet):
    # Grab the data about planting offset and soaking time from harvest_offset sheet
    result = sheet.values().get(spreadsheetId=MICROGREENS_SPREADSHEET_ID,
                                range=HARVEST_OFFSET).execute()

    values = result.get('values', [])

    # Collect first column
    first_column = [item[0] for item in values]

    # Remove first column
    [item.pop(0) for item in values]

    new_dict = {}

    for i in range(values[0].__len__()):
        column = [item[i] for item in values]
        new_dict[column[0]] = {first_column[1]: column[1], first_column[2]: column[2]}

    print("dict of harvest_offset", new_dict)
    return new_dict

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    read_harvest_offset(sheet)
    result = sheet.values().get(spreadsheetId=MICROGREENS_SPREADSHEET_ID,
                                range=CONTACT_RANGE).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            print(row)


if __name__ == '__main__':
    main()