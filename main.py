import requests

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
       return [response.status_code, response.text]
    else:
       return [response.status_code, response.text]
    
  def getRequest(self, url, headers):
      response = requests.get(url=url, headers=headers)
      return response.text, response.status_code
  
API = SpotifyAPI()
print(API.requestAccessToken())

headers = {
    "Authorization": f"Bearer {API.accessToken}"
}

text, code = API.getRequest("https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb", headers)

print(text)