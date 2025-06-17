import requests
from SpotifyAPI import SpotifyAPI
  
API = SpotifyAPI()
#print(API.requestAccessToken())
API.authenticateUser()

#print(API.authUser.current_user())

headers = {
    "Authorization": f"Bearer {API.accessToken}",
    "limit" : "50"
}

url = "https://api.spotify.com/v1/me/playlists"

response = API.getPlaylistItems("https://open.spotify.com/playlist/5upr6hJW02oedibLwpAwvj?si=8513499a9b0949d7")

for i in response['items']:
  print(i['name'])