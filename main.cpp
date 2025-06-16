#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <curl/curl.h>
#include "SpotifyAPI.h"




int main(int argc, char const *argv[])
{
  std::cout << "real";
  std::unordered_map<std::string, std::string> env = SpotifyAPI::loadEnv();
  std::cout << "API_key: " << env["API_KEY"] << "\n";
  std::cout << SpotifyAPI::newAccessToken() << std::endl;

  return 0;
}
