// main.cpp
#include <iostream>

int main() {
    // Überprüfen, ob die benutzerdefinierte Variable definiert ist
    #ifdef CUSTOM_VARIABLE
        std::cout << "Custom Variable in main.cpp: " << CUSTOM_VARIABLE << std::endl;
    #else
        std::cout << "Custom Variable is not defined in main.cpp." << std::endl;
    #endif

    return 0;
}
