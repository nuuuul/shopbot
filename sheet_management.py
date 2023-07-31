import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

import time

import data_base as db

CREDENTIALS_FILE = 'credentials.json'  # Имя файла с закрытым ключом, вы должны подставить свое
empty_row = 0

# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())  # Авторизуемся в системе
service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)  # Выбираем работу с таблицами и 4 версию API

spreadsheetId = '1J2lyk7camMVfQ8PcT3232OfF09V3E_CKZ0SRDE4S_j0'  # сохраняем идентификатор файла


def first_free(list):
    results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                       ranges=[list + "!A1:A1"],
                                                       valueRenderOption='FORMATTED_VALUE',
                                                       dateTimeRenderOption='FORMATTED_STRING').execute()
    i = 1
    while 'values' in results['valueRanges'][0]:
        i = i + 1
        ranges = [list + "!A" + str(i) + ":A" + str(i)]
        results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                           ranges=ranges,
                                                           valueRenderOption='FORMATTED_VALUE',
                                                           dateTimeRenderOption='FORMATTED_STRING').execute()
        time.sleep(1)
    return i


def finduuid(uuid, list='В формировании'):
    results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                       ranges=[list + "!A2:G2"],
                                                       valueRenderOption='FORMATTED_VALUE',
                                                       dateTimeRenderOption='FORMATTED_STRING').execute()
    i = 2
    while 'values' in results['valueRanges'][0]:
        ranges = [list + "!A" + str(i) + ":G" + str(i)]
        results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                           ranges=ranges,
                                                           valueRenderOption='FORMATTED_VALUE',
                                                           dateTimeRenderOption='FORMATTED_STRING').execute()
        string = results['valueRanges'][0]['values'][0]

        if string[0] == str(uuid) and len(string) < 7:
            return i
        i = i + 1

    return first_free(list)


def insert_id(text):
    i = first_free('В формировании')
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "В формировании!A" + str(i) + ":A" + str(i),
             "majorDimension": "ROWS",
             "values": [
                 [text]
             ]}
        ]
    }).execute()


def insert(userid, text, col_num):
    i = finduuid(userid)
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "В формировании!" + col_num + str(i) + ":" + col_num + str(i),
             "majorDimension": "ROWS",
             "values": [
                 [text]
             ]}
        ]
    }).execute()


def copy(userid):
    i = finduuid(userid)
    ranges = ["В формировании!A" + str(i) + ":G" + str(i)]
    results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                       ranges=ranges,
                                                       valueRenderOption='FORMATTED_VALUE',
                                                       dateTimeRenderOption='FORMATTED_STRING').execute()
    request_body = {
      "requests": [
        {
          "deleteDimension": {
            "range": {
              "sheetId": '901057824',
              "dimension": "ROWS",
              "startIndex": i,
              "endIndex": i
            }
          }
        },
        {
          "deleteDimension": {
            "range": {
              "sheetId": '901057824',
              "dimension": "COLUMNS",
              "startIndex": 1,
              "endIndex": 7
            }
          }
        },
      ],
    }
    service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheetId,
        body=request_body
    ).execute()

    i = first_free('1')
    service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Сформированные заказы!A" + str(i) + ":H" + str(i),
             "majorDimension": "ROWS",
             "values": [results['valueRanges'][0]['values'][0]]}
        ]
    }).execute()


def insert_all(userid):
    records = db.get_row(userid)
    i = empty_row
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Сформированные заказы!A" + str(i) + ":I" + str(i),
             "majorDimension": "ROWS",
             "values": [
                 records[0]
             ]}
        ]
    }).execute()
    db.delete_id(userid)




# ranges = ["В формировании!A3:E3"]
# results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
#                                                    ranges=ranges,
#                                                    valueRenderOption='FORMATTED_VALUE',
#                                                    dateTimeRenderOption='FORMATTED_STRING').execute()
# print(results['valueRanges'][0]['values'][0])
