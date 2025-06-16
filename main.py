import requests
from SpotifyAPI import SpotifyAPI
  
API = SpotifyAPI()
print(API.requestAccessToken())

headers = {
    "Authorization": f"Bearer {API.accessToken}"
}

text, code = API.getRequest("https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb", headers)

print(text)