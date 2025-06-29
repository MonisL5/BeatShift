from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def get_youtube_client():
    scopes = ["https://www.googleapis.com/auth/youtube"]
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes)
    credentials = flow.run_local_server(port=0)
    return build("youtube", "v3", credentials=credentials)
