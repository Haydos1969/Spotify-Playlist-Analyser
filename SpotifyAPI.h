#pragma once
#include <string>
#include <unordered_map>

class SpotifyAPI {
  private:
    static std::string accessToken;
  public:
    static std::unordered_map<std::string, std::string> loadEnv();
  
    static std::string newAccessToken();
};

