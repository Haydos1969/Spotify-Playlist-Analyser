import requests, json, spotipy 
from spotipy.oauth2 import SpotifyOAuth

class SpotifyAPI:
   def __init__(self):
      # Reads the .env and initalises the api key and client ID
      env_vars = {}
      with open(".env") as f:
         for line in f:
               line = line.strip()
               if line and not line.startswith("#"):
                  key, value = line.split("=", 1)
                  env_vars[key.strip()] = value.strip()
      self.API_KEY = env_vars["API_KEY"]
      self.CLIENT_ID = env_vars["CLIENT_ID"]

  
   def requestAccessToken(self):
    url = "https://accounts.spotify.com/api/token"
    data = {
       "grant_type" : "client_credentials",
       "client_id" : self.CLIENT_ID,
       "client_secret" : self.API_KEY
    }
    
    response = requests.post(url, data=data)

    if response.ok:
       accessToken = response.json()
       self.accessToken = accessToken.get("access_token")
       return [response.text, response.status_code]
    else:
       return [response.text, response.status_code]
   
   def authenticateUser(self):
      sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
         client_id=self.CLIENT_ID,
         client_secret= self.API_KEY,
         redirect_uri="http://127.0.0.1:8888/callback",
         scope="user-library-read user-read-private playlist-read-private playlist-read-collaborative"
      ))
      self.authUser = sp

      with open('.cache', 'r') as f:
         cacheData = json.load(f)
      if (cacheData["access_token"]):
         self.accessToken = cacheData['access_token']
      else:
         print("No access token found")


   def getRequest(self, url, headers):
         response = requests.get(url=url, headers=headers)
         return response.json(), response.status_code