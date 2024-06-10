from dotenv import load_dotenv
import os

load_dotenv()

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI')