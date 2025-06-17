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

response, statusCode = API.getRequest(url, headers)

for i in response["items"]:
  print(i['name'])