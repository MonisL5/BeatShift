def get_playlist_tracks(sp, playlist_id):
    playlist = sp.playlist(playlist_id)
    playlist_name = playlist["name"]

    tracks = []
    results = sp.playlist_tracks(playlist_id)

    while results:
        for item in results["items"]:
            track = item["track"]
            title = track["name"]
            artist = track["artists"][0]["name"]
            tracks.append((title, artist))

        if results["next"]:
            results = sp.next(results)
        else:
            break

    return playlist_name, tracks
