import requests
from SpotifyAPI import SpotifyAPI
  
API = SpotifyAPI()
#print(API.requestAccessToken())
API.authenticateUser()

print(API.authUser.current_user())

headers = {
    "Authorization": f"Bearer {API.accessToken}"
}

spotifyID = "nh6wd77lqlracq6pb203uol6o"#input("Enter Your Spotify ID: ")
url = "https://api.spotify.com/v1/users/" + spotifyID + "/playlists"
