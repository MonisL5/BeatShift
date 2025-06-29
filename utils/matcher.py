def search_youtube_video(yt, query):
    request = yt.search().list(q=query, part="snippet", maxResults=1, type="video")
    response = request.execute()
    items = response.get("items", [])
    if items:
        return items[0]["id"]["videoId"]
    return None
