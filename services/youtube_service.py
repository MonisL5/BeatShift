import time
import random
from googleapiclient.errors import HttpError

def create_youtube_playlist(yt, title):
    body = {
        "snippet": {
            "title": title,
            "description": "Playlist migrated from Spotify via BeatShift"
        },
        "status": {
            "privacyStatus": "private"
        }
    }
    try:
        request = yt.playlists().insert(part="snippet,status", body=body)
        response = request.execute()
        print(f"✅ YouTube playlist created: {response['id']}")
        return response["id"]
    except HttpError as e:
        print(f"❌ Failed to create YouTube playlist: {e}")
        return None

def add_tracks_to_youtube(yt, playlist_id, video_id, max_retries=5):
    body = {
        "snippet": {
            "playlistId": playlist_id,
            "resourceId": {
                "kind": "youtube#video",
                "videoId": video_id
            }
        }
    }

    for attempt in range(max_retries):
        try:
            yt.playlistItems().insert(part="snippet", body=body).execute()
            time.sleep(1.5)
            return
        except HttpError as e:
            if e.resp.status in [403, 409, 429, 500, 503]:
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                print(f"⚠️ Attempt {attempt + 1}: YouTube API returned {e.resp.status} - retrying in {wait_time:.2f}s")
                time.sleep(wait_time)
            else:
                print(f"❌ Unhandled error: {e}")
                break
    print(f"❌ Skipped video ID {video_id} after {max_retries} failed attempts.")
