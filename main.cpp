#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>

std::unordered_map<std::string, std::string> loadEnv() {
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


int main(int argc, char const *argv[])
{
  std::unordered_map<std::string, std::string> envVars = loadEnv();
  std::cout << "api_key: " << envVars["API_KEY"] << "\n";
  return 0;
}
