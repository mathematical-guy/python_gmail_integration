from base_client import GoogleClient


def is_client_configured_properly(func):
    def inner(self: GoogleClient, *args, **kwargs):
        if self.service is None:
            raise Exception('Service is not configured properly')

        if self.creds is None:
            raise Exception('Credentials are not configured properly')

        print(f"Client {str(self)} configured properly, executing {str(func)}")
        func(self, *args, **kwargs)

    return inner
