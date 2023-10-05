import os.path
import sys
import requests

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
          'https://www.googleapis.com/auth/photoslibrary.readonly',
          'https://www.googleapis.com/auth/photoslibrary.appendonly']

def get_creds():

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds


def drive_auth():
    creds = get_creds()
    try:
        return build('drive', 'v3', credentials=creds)
    except:
        e = sys.exc_info()[0]
        # TODO(developer) - Handle errors individually
        print(f'An error occurred: {e}')
        raise()

def photos_auth():
    creds = get_creds()
    try:
        return build('drive', 'v3', credentials=creds)
    except:
        e = sys.exc_info()[0]
        # TODO(developer) - Handle errors individually
        print(f'An error occurred: {e}')
        raise()

def get_albums():
    creds = get_creds()
    albums = requests.get('https://photoslibrary.googleapis.com/v1/albums',
                          headers={'Content-Type':'application/json',
                                   'Authorization':f'Bearer {creds.token}'})
    print ('Got albums')

def upload():
    creds = get_creds()
    with open('/Users/aramachandran/Downloads/test.jpeg', 'rb') as f:
        data = f.read()
    retval = requests.post('https://photoslibrary.googleapis.com/v1/uploads',
                            data = data,
                            headers={'Content-Type':'application/octet-stream',
                                   'Authorization':f'Bearer {creds.token}',
                                   'X-Goog-Upload-Content-Type': 'mime-type',
                                   'X-Goog-Upload-Protocol': 'raw',
                                   })
    print('Upload done')
    upload_token = retval.text
    json = {
        'newMediaItems': [
            {
                'description': 'testing upload using photos api',
                'simpleMediaItem': {
                    'fileName': 'test.jpeg',
                    'uploadToken': upload_token
                }
            }
        ]
    }
    retval = requests.post('https://photoslibrary.googleapis.com/v1/mediaItems:batchCreate',
                            json = json,
                            headers={'Content-Type':'application/json',
                                   'Authorization':f'Bearer {creds.token}',
                                   })
    print('Media item created')
