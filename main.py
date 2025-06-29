from auth.spotify_auth import get_spotify_client
from auth.youtube_auth import get_youtube_client
from services.spotify_service import get_playlist_tracks
from services.youtube_service import create_youtube_playlist, add_tracks_to_youtube
from utils.matcher import search_youtube_video

def main():
    sp = get_spotify_client()
    yt = get_youtube_client()

    playlist_id = input("Enter your Spotify Playlist ID: ")
    playlist_name, tracks = get_playlist_tracks(sp, playlist_id)

    print(f"\nMigrating Playlist: {playlist_name} with {len(tracks)} tracks\n")

    yt_playlist_id = create_youtube_playlist(yt, playlist_name)

    for track in tracks:
        print(f"Searching YouTube for: {track}...")
        video_id = search_youtube_video(yt, track)
        if video_id:
            add_tracks_to_youtube(yt, yt_playlist_id, video_id)
            print(f"Added: {track}\n")
        else:
            print(f"Not found on YouTube: {track}\n")

    print("\nPlaylist migration complete.")

if __name__ == "__main__":
    main()
