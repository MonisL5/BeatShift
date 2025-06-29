# BeatShift 

Python tool to migrate Spotify playlists to YouTube Music using APIs.

## Features
- OAuth-secure login for both platforms
- Automatic song matching via metadata
- Custom YouTube playlist creation

## Setup

1. Clone the repo:
git clone https://github.com/YOUR_USERNAME/BeatShift.git
cd BeatShift

cpp
Copy
Edit

2. Create and activate virtual environment:
python -m venv venv
venv\Scripts\activate

markdown
Copy
Edit

3. Install dependencies:
pip install -r requirements.txt

bash
Copy
Edit

4. Create a `.env` file and set:
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback

markdown
Copy
Edit

5. Download your `client_secret.json` from Google and place it in root.

6. Run:
python main.py

markdown
Copy
Edit

## Notes
- You'll need your own Spotify and YouTube Developer credentials.
- This app respects API quotas and handles retry logic.

## License
MIT