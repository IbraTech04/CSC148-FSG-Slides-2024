import spotipy
from spotipy.oauth2 import SpotifyOAuth
from typing import List
import os
from dotenv import load_dotenv
load_dotenv("Week 7 - List Comprehensions/tokens.env")

# NOTE: THIS FILE IS PROVIDED OUTSIDE THE FSG. THIS IS IRRELEVANT TO THE FSG. THIS IS JUST A FILE THAT I USED TO SCRAPE SONGS FROM SPOTIFY.
# I only put it here in case anyone was curious how i scraped music from spotify

# I better not see anyone asking "omg i can't understand this code am i screwed for post?!?!?!" because like i said above; this code is irrelevant to the FSG and to the course. Just here for anyone curious about how to scrape music from spotify.


class Song:
    title: str
    _liked: bool
    genre: str
    
    def __init__(self, title: str, liked: bool, genre: str):
        self.title = title
        self._liked = liked
        self.genre = genre
    
    def is_like(self):
        return self._liked

    def __str__(self):
        return f'Song("{self.title}", {self._liked}, "{self.genre}"), '

# Function to authenticate with Spotify API using OAuth
def authenticate_spotify():
    # Set up OAuth authentication
    scope = "user-library-read"
    client_id = os.environ.get("CLIENT_ID")
    client_secret = os.environ.get("CLIENT_SECRET")
    sp_oauth = SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri="http://localhost:8888/callback")
    
    # Get token (.cache file)
    token_info = sp_oauth.get_cached_token()
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        print(f"Please visit this URL to authorize access: {auth_url}")
        response = input("Enter the URL you were redirected to: ")
        code = sp_oauth.parse_response_code(response)
        token_info = sp_oauth.get_access_token(code)
    
    # Authenticate using the obtained token
    return spotipy.Spotify(auth=token_info['access_token'])

# Function to extract songs from a playlist URL
def extract_playlist_songs(playlist_url: str):
    sp = authenticate_spotify()
    
    # Extract playlist ID from the URL
    playlist_id = playlist_url.split('/')[-1]
    
    # Get playlist tracks
    results = sp.playlist_tracks(playlist_id)
    
    songs = []
    for item in results["tracks"]['items']:
        track = item['track']
        title = track['name']
        # Get whether the song is liked from the user library
        liked = sp.current_user_saved_tracks_contains([track['id']])[0]

        artist = sp.artist(track['artists'][0]['id'])
        genre = artist['genres'][0] if artist['genres'] else ""
        # Format genre to have consistent capitalization
        genre = genre.capitalize()
        songs.append(Song(title, liked, genre))
    
    return songs


# Example usage
if __name__ == "__main__":
    playlist_url = "https://open.spotify.com/playlist/1VrPlCMtYByylvqKWYqlK2?si=1a47c5d6b0684ad6"
    
    songs = extract_playlist_songs(playlist_url)

    print(f"[{''.join([str(song) for song in songs])}]") #Ha! Another List Comprehension!
