#include "SpotifyAPI.h"
#include <string>
#include <curl/curl.h>
#include <unordered_map>
#include <fstream>
#include <sstream>
#include <nlohmann/json.hpp>
#include <iostream>
using json = nlohmann::json;

std::string SpotifyAPI::accessToken = "";

std::unordered_map<std::string, std::string> SpotifyAPI::loadEnv() {
  std::unordered_map<std::string, std::string> envVars;
  std::ifstream file(".env");
  std::string line;

  while (std::getline(file, line)) {
      if (line.empty() || line[0] == '#') continue;

      size_t equals = line.find('=');
      if (equals != std::string::npos) {
          std::string key = line.substr(0, equals);
          std::string value = line.substr(equals + 1);
          envVars[key] = value;
      }
  }

  return envVars;
}

std::string SpotifyAPI::newAccessToken() {
  CURL* curl = curl_easy_init();
  std::string responseString;
  std::string accessToken;
  
  if (curl) { 
    std::unordered_map<std::string, std::string> envVars = loadEnv();
    std::string body = "grant_type=client_credentials&client_id=" + envVars["CLIENT_ID"] + "&client_secret=" + envVars["API_KEY"];

    curl_easy_setopt(curl, CURLOPT_URL, "https://accounts.spotify.com/api/token");
    curl_easy_setopt(curl, CURLOPT_POST, 1L);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, body.c_str());

    // Set headers
    struct curl_slist* headers = nullptr;
    headers = curl_slist_append(headers, "Content-Type: application/x-www-form-urlencoded");
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, [](char* ptr, size_t size, size_t nmemb, void* userdata) -> size_t {
            size_t totalSize = size * nmemb;
            std::string* response = static_cast<std::string*>(userdata);
            response->append(ptr, totalSize);
            return totalSize;
    });
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &responseString);
    
    CURLcode res = curl_easy_perform(curl);
    std::cout << "Raw response: " << responseString << std::endl;

    if (res == CURLE_OK) {
      try {
        json parsed = json::parse(responseString);
        accessToken = parsed["access_token"];
      } catch (...) {
        accessToken = "";
      }
    }
    else {
      std::cerr << "curl_easy_perform() failed: " << curl_easy_strerror(res) << std::endl;
    }

    // Cleanup
    curl_easy_cleanup(curl);
    curl_slist_free_all(headers);

  }

  SpotifyAPI::accessToken = accessToken;

  return accessToken;
}