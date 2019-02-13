from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

SECRET_FOLDER = './src'
CRED_FILE = 'client_secret.json'
TOKEN = 'token.pickle'

TOKEN_PATH = os.path.join(SECRET_FOLDER, TOKEN)

def main():
    """
    credsはクライアントキーからトークンを発行する
    """
    creds = None

    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'rb') as token:
            creds = pickle.load(token)
    #もし既にトークンを発行して居た場合はrefreshする
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.join(SECRET_FOLDER, CRED_FILE), SCOPES)
            creds = flow.run_local_server()
        #新規トークン生成
        with open(TOKEN_PATH, 'wb') as token:
            pickle.dump(creds, token)

    #作ったcredsを使ってサービスオブジェクト生成
    service = build('calendar', 'v3', credentials=creds)

    #直近10件のイベントを取得する
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

if __name__ == '__main__':
    main()