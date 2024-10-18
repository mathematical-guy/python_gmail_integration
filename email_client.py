from base_client import GoogleClient

SCOPES = []


class EmailClient(GoogleClient):
    """ Google Client restricted to Email Service only """
    def __init__(self, *args, **kwargs):
        super().__init__(service_name='gmail', *args, **kwargs)

    def list_emails(self):
        results = self.service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=10).execute()
        messages = results.get('messages', [])

        if not messages:
            print("No messages found.")

        else:
            print("Messages:")
            for message in messages:
                msg = self.service.users().messages().get(userId='me', id=message['id']).execute()
                print(f"Message snippet: {msg['snippet']}")


if __name__ == '__main__':
    client = EmailClient()
    client.list_emails()
