import os
import requests
from dotenv import dotenv_values,load_dotenv
from requests.auth import HTTPBasicAuth
from json_parser import SpotifyData

load_dotenv()
spotify_auth= os.getenv("SPOTIFY_KEY")
spotify_base_url = os.getenv("SPOTIFY_URL")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
auth_url = os.getenv('SPOTIFY_AUTH_URL')

class SpotifyScraper:
    def get_access_token():
        response = requests.post(
            auth_url,
            data={'grant_type': 'client_credentials'},
            auth=HTTPBasicAuth(spotify_auth, spotify_client_secret)
        )
        if response.status_code == 200:
            return response.json()['access_token']
        else:
            raise Exception("Failed to retrieve access token")

    def search_album(name):
        access_token = SpotifyScraper.get_access_token()
        headers = {'Authorization': f'Bearer {access_token}'}
        base_url = f"{spotify_base_url}search"
        params = {
            'q':name,
            'type':'album',
            'limit':1
        }
        response = requests.get(base_url, headers=headers, params=params)
        if response.status_code ==200:
            data= response.json()
            
            if data['albums']['items']:
                album = data['albums']['items'][0]
                id= album['id']
                tracks_url = f"{spotify_base_url}albums/{id}/tracks"
                tracks_response = requests.get(tracks_url, headers=headers)
                if tracks_response.status_code == 200:
                    tracks_data = tracks_response.json()
                    spotify_data=SpotifyData.from_json(tracks_data)
                    list_of_songs=[]
                    for item in spotify_data.items:
                        song_name= item.name
                        artists=[]
                        for artist in item.artists:
                            artist_name= artist.name
                            
                            artists.append(artist_name)

                        list_of_songs.append(
                            {
                                "song_name":song_name,
                                "artists":artists
                            }
                        )
                    return list_of_songs

        else:
            print("error")


SpotifyScraper.search_album('jawan')




# # main.py
# from spotify_models import SpotifyData

# Sample JSON data (replace this with actual JSON data in practice)
# json_data = {
#     "href": "https://api.spotify.com/v1/tracks",
#     "items": [
#         {
#             "artists": [
#                 {
#                     "external_urls": {"spotify": "https://spotify.com/artist1"},
#                     "href": "https://api.spotify.com/v1/artists/1",
#                     "id": "1",
#                     "name": "Artist 1",
#                     "type": "artist",
#                     "uri": "spotify:artist:1"
#                 }
#             ],
#             "available_markets": ["US", "CA"],
#             "disc_number": 1,
#             "duration_ms": 200000,
#             "explicit": False,
#             "external_urls": {"spotify": "https://spotify.com/track1"},
#             "href": "https://api.spotify.com/v1/tracks/1",
#             "id": "1",
#             "name": "Track 1",
#             "preview_url": None,
#             "track_number": 1,
#             "type": "track",
#             "uri": "spotify:track:1",
#             "is_local": False
#         }
#     ]
# }

# # Create SpotifyData object from JSON data
# spotify_data = SpotifyData.from_json(json_data)
# print("Parsed SpotifyData object:", spotify_data.name)

# Convert SpotifyData object back to JSON
# json_output = spotify_data.to_json()
# print("Converted back to JSON:", json_output.items.artists)
