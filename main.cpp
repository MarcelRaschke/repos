// main.cpp
#include <iostream>

int main() {
    // Überprüfen, ob die benutzerdefinierte Variable definiert ist
    #ifdef CUSTOM_VARIABLE
        std::cout << "Custom Variable: " << CUSTOM_VARIABLE << std::endl;
    #else
        std::cout << "Custom Variable is not defined." << std::endl;
    #endif

    return 0;
}
# CMakeLists.txt
cmake_minimum_required(VERSION 3.10)
project(MyProject VERSION 1.0)

# Benutzerdefinierte Variable verwenden
message(STATUS "Custom Variable: ${CUSTOM_VARIABLE}")

# Übergabe der benutzerdefinierten Variablen als Präprozessor-Direktive
add_definitions(-DCUSTOM_VARIABLE="${CUSTOM_VARIABLE}")

# Weitere CMake-Befehle...
{
  "configurations": [
    {
      "name": "Debug",
      "generator": "Ninja",
      "buildRoot": "${workspaceRoot}/build/${name}",
      "cmakeCommandArgs": "-DCUSTOM_VARIABLE=DebugValue -DCMAKE_CXX_FLAGS_DEBUG='-Wall -O0'",
      "buildCommandArgs": "",
      "ctestCommandArgs": "",
      "inheritEnvironments": [ "msvc_x64" ]
    },
    {
      "name": "Release",
      "generator": "Ninja",
      "buildRoot": "${workspaceRoot}/build/${name}",
      "cmakeCommandArgs": "-DCUSTOM_VARIABLE=ReleaseValue -DCMAKE_CXX_FLAGS_RELEASE='-O3'",
      "buildCommandArgs": "",
      "ctestCommandArgs": "",
      "inheritEnvironments": [ "msvc_x64" ]
    }
  ]
}
