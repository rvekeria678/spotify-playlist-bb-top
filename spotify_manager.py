import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from config.spotipy import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
from pprint import pprint
import os
import base64

class SpotifyManager:
    def __init__(self) -> None:
        SCOPES = ['playlist-modify-private', 'user-library-read']
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPES, redirect_uri=SPOTIFY_REDIRECT_URI))

        self.user = self.sp.current_user()
        self.user_id = self.user['id']
        self.progress = 0
        self.playlist_size = 0

    def create_playlist(self, playlist_data: tuple) -> None:
        self.playlist_size = len(playlist_data[1])
        try:
            playlist_name = f'{playlist_data[0]} Billboard 100'
            playlist_description = "A playlist created with Spotipy"
            playlist = self.sp.user_playlist_create(self.user_id,
                                               playlist_name,
                                               public=False,
                                               description=playlist_description)
            playlist_id = playlist['id']
            print(f"Playlist created with ID: {playlist_id}")
            print("Attempting to add songs...")
            results = [self.search(track_name=track,
                                  release_year=playlist_data[0].split('-')[0])
                                  for track in playlist_data[1]]
            uri_links = [result['tracks']['items'][0]['uri'] for result in results if result['tracks']['items']]
            self.sp.user_playlist_add_tracks(user=self.user_id,playlist_id=playlist_id, tracks=uri_links)
            print("Succesfully Added Songs! Enjoy your tunes!")
            self.progress = 0

        except spotipy.exceptions.SpotifyException:
            print("Authentication failed. Check you credentials.")

    def search(self, track_name: str, release_year: str):
        query = f"track:{track_name} year:{release_year}"
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Progress :- {int((self.progress/self.playlist_size)*100)}% | Searching for {track_name} : ")
        result = self.sp.search(q=query, limit=1, type='track')
        self.progress += 1
        return result