import httplib2
from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.http import MediaFileUpload
CREDENTIALS_FILE = 'credentials.json'  # Имя файла с закрытым ключом, вы должны подставить свое
# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())  # Авторизуемся в системе
driveService = discovery.build('drive', 'v3', http=httpAuth)
def upload_basic(name):
    file_metadata = {'name': name}
    media = MediaFileUpload(name,
                            mimetype='image/jpg')
    # pylint: disable=maybe-no-member
    file = driveService.files().create(body=file_metadata, media_body=media,
                                       fields='webViewLink, id').execute()
    access = driveService.permissions().create(
        fileId=file.get('id'),
        body={'type': 'anyone', 'role': 'writer'},
        fields='id'
    ).execute()
    return file.get("webViewLink")
