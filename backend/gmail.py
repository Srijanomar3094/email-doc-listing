from fastapi import APIRouter
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

router = APIRouter()
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    creds = flow.run_local_server(port=0)
    return creds

@router.get("/emails")
def list_emails():
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=10).execute()
    messages = results.get('messages', [])

    emails = []
    for msg in messages:
        data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = data['payload']['headers']
        subject = sender = date = "N/A"
        for h in headers:
            if h['name'] == 'From':
                sender = h['value']
            elif h['name'] == 'Subject':
                subject = h['value']
            elif h['name'] == 'Date':
                date = h['value']
        attachments = []
        parts = data['payload'].get('parts', [])
        for part in parts:
            if 'filename' in part and part['filename']:
                attachments.append(part['filename']) 
        emails.append({
            "sender": sender,
            "subject": subject,
            "timestamp": date,
            "attachments": attachments
        })
    return emails
