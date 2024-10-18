import os
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class GoogleClient:
    """ Google Client abstract for Google Services """
    def __init__(self, service_name=None, scopes=[]):
        self.SCOPE = scopes
        self.service_name = service_name
        self.creds = None
        self.service = None

        self.__handle_authentication()      # Authenticate for provided 'credentials.json' file
        self.__build_service()              # Build Service object, which will interact with API endpoints

    def __build_service(self):
        self.service = build(serviceName=self.service_name, version='v1', credentials=self.creds)

    def __handle_authentication(self):
        if os.path.exists('token.pickle'):      # For already logged-in User, retrieve token file
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    client_secrets_file='credentials.json', scopes=self.SCOPE)
                self.creds = flow.run_local_server(port=8080)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)
