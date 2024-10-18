import sqlite3
from sqlite3 import Connection, Cursor


class DatabaseClient:
    def __init__(self):
        self.connection: Connection = sqlite3.connect(database='emails.db')
        self.cursor: Cursor = self.connection.cursor()

        # Create the emails table
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email_id TEXT UNIQUE NOT NULL,
            sender TEXT,
            subject TEXT,
            snippet TEXT,
            date_received TEXT
        )
        ''')

        self.connection.commit()
        # self.connection.close()

    def __exit__(self, *args, **kwargs):
        self.connection.close()

    def insert_email_into_database(self, email: dict):
        email_id = email['email_id']
        snippet = email['snippet']
        sender = email['sender']
        subject = email['subject']
        date_received = email['date_received']

        try:
            self.cursor.execute('''
                INSERT OR IGNORE INTO emails (email_id, sender, subject, snippet, date_received)
                VALUES (?, ?, ?, ?, ?)
                ''', (email_id, sender, subject, snippet, date_received))

            self.connection.commit()

        except Exception as e:
            print(f"Error {str(e)} occurred while inserting email {snippet}")

