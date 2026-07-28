#!/usr/bin/env python3
"""
Simple Gmail sender script using Gmail API
Sends the resume/cover letter request email
"""

import base64
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail():
    """Authenticate with Gmail API"""
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def send_email(to_email, subject, body):
    """Send email via Gmail API"""
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)

    message = MIMEText(body)
    message['to'] = to_email
    message['subject'] = subject

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    send_message = {'raw': raw_message}

    try:
        result = service.users().messages().send(userId='me', body=send_message).execute()
        print(f"✅ Email sent successfully!")
        print(f"Message ID: {result['id']}")
        return result
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        raise

if __name__ == '__main__':
    to_email = 'anissavalentin2000@gmail.com'
    subject = 'Opportunity - Resume & Cover Letter Request'
    body = """Hi,

I hope this email finds you well.

I wanted to reach out regarding some exciting opportunities that may be a great fit for your background and experience.

To move forward, could you please send me:

1. Your resume
2. A cover letter highlighting your interest in these opportunities

Looking forward to hearing from you.

Best regards"""

    send_email(to_email, subject, body)
