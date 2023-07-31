from __future__ import print_function
import os.path
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SAMPLE_RANGE_NAME = 'Сформированные заказы!A1:I1'

class GoogleSheet:
    SPREADSHEET_ID = '1J2lyk7camMVfQ8PcT3232OfF09V3E_CKZ0SRDE4S_j0'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    service = None

    def __init__(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print('flow')
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secrets.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    def updateRangeValues(self, range, values):
        data = [{
            'range': range,
            'values': values
        }]
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }
        result = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.SPREADSHEET_ID, body=body).execute()
        print('{0} cells updated.'.format(result.get('totalUpdatedCells')))

        
def main():
   gs = GoogleSheet()
   test_range = 'Сформированные заказы!G2:H4'
   test_values = [
       [16, 26],
       [36, 46],
       [56, 66]
   ]
   gs.updateRangeValues(test_range, test_values)

if __name__ == '__main__':
    main()








# Подключаем библиотеки
# import httplib2
# from googleapiclient import discovery
# from oauth2client.service_account import ServiceAccountCredentials
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# 
# CREDENTIALS_FILE = 'credentials.json'  # Имя файла с закрытым ключом, вы должны подставить свое

# Читаем ключи из файла
# credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

# httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
# service = discovery.build('sheets', 'v4', http=httpAuth) # Выбираем работу с таблицами и 4 версию API
# 
# spreadsheet = service.spreadsheets().create(body = {
    # 'properties': {'title': 'Первый тестовый документ', 'locale': 'ru_RU'},
    # 'sheets': [{'properties': {'sheetType': 'GRID',
                            #    'sheetId': 0,
                            #    'title': 'Лист номер один',
                            #    'gridProperties': {'rowCount': 100, 'columnCount': 15}}}]
# }).execute()
# spreadsheetId = spreadsheet['spreadsheetId'] # сохраняем идентификатор файла
# print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)
# 
# 
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()


#driveService = discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API
#access = driveService.permissions().create(
#    fileId = '1J2lyk7camMVfQ8PcT3232OfF09V3E_CKZ0SRDE4S_j0',
#    body = {'type': 'anyone', 'role': 'writer'},  # Открываем доступ на редактирование
#    fields = 'id'
#).execute()