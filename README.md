# Gmail API Integration with SQLite

This project demonstrates how to authenticate with Google's Gmail API using OAuth, fetch emails from your inbox, store them in an SQLite database, and apply dynamic filters based on user input. The filters are defined in a JSON file, and the user can apply multiple rules with AND/OR operators.



## Features
- Authenticate with the Gmail API using OAuth 2.0
- Fetch a list of emails from Gmail
- Store fetched emails in an SQLite database
- Apply multiple filter rules (conditions) using dynamic SQL queries
- Support for AND/OR operators between rules 
- Rules and filters stored in a JSON file for flexibility



https://github.com/user-attachments/assets/fc94dcd0-b9f2-40ce-aeb1-b09020aebe5e



## Requirements
- Python 3.x
- Google API Python client (google-auth, google-auth-oauthlib, google-api-python-client)
- SQLite3

### Install Dependencies
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

### Clone the Repository
 - git clone https://github.com/mathematical-guy/python_gmail_integration/
 - cd python_gmail_integration

### Google API Setup
- Go to the Google Cloud Console.
- Create a new project (or select an existing project).
- Enable the Gmail API under APIs & Services.
- Create OAuth 2.0 credentials under Credentials:
- Select Desktop Application as the application type.
- Download the credentials (client_secret.json) and save it to the project directory.

### Run the Application
- python email_client.py    -> Fetches Email based on client_secret credentials for web app
- python process_email.py   -> Processes & Filter email based on user input 

Note: A database file is created emails.db while executing email_client.py 


## Troubleshooting
### Error: Access blocked: Authorization Error
    If you encounter an Authorization Error during authentication:

    Make sure the redirect URI in your OAuth credentials matches the one in your Python code.
    Ensure that the Gmail API is enabled in the Google Cloud Console.
    Check the OAuth consent screen configuration.
    
    Error: redirect_uri_mismatch
    Ensure that the redirect URI used in your app matches the one set in the Google Cloud Console.
