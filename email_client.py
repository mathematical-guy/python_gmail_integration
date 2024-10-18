from base_client import GoogleClient

from utils import is_client_configured_properly
from database import DatabaseClient

SCOPES = []


class EmailClient(GoogleClient):
    """ Google Client restricted to Email Service only """
    def __init__(self, *args, **kwargs):
        super().__init__(service_name='gmail', *args, **kwargs)

    def __parse_email(self, message: dict):
        subject = "No Subject"
        sender = "Unknown"
        date_received = "Unknown"

        email_id = message['id']
        snippet = message['snippet']

        headers: list = message['payload']['headers']
        for header in headers:
            header: dict = header
            header_name = header.get('name')
            header_value = header.get('value')

            if header_name == 'Subject':
                subject = header_value

            elif header_name == 'FROM':
                sender = header_value

            elif header_name == 'Date':
                date_received = header_value

        return {
            "email_id": email_id, "snippet": snippet, "date_received": date_received,
            "sender": sender, "subject": subject,
        }

    @is_client_configured_properly
    def list_emails(self):
        results = self.service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=10).execute()
        messages = results.get('messages', [])

        if not messages:
            print("No messages found.")

        else:
            database = DatabaseClient()
            print("Messages:")
            for message in messages:
                msg = self.service.users().messages().get(userId='me', id=message['id']).execute()
                print(f"Message snippet: {msg['snippet']}")
                email = self.__parse_email(message=msg)
                database.insert_email_into_database(email=email)


if __name__ == '__main__':
    client = EmailClient()
    client.list_emails()
