import requests
from SpotifyAPI import SpotifyAPI
  
API = SpotifyAPI()
print(API.requestAccessToken())

headers = {
    "Authorization": f"Bearer {API.accessToken}"
}

spotifyID = "nh6wd77lqlracq6pb203uol6o"#input("Enter Your Spotify ID: ")
url = "https://api.spotify.com/v1/users/" + spotifyID + "/playlists"


text, code = API.getRequest(url, headers)
print(type(text))
for i in text["items"]:
  print(i["name"])