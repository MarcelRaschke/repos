// my_library/config.h
#ifndef CONFIG_H
#define CONFIG_H

#include <iostream>

void printCustomVariable() {
    // Überprüfen, ob die benutzerdefinierte Variable definiert ist
    #ifdef CUSTOM_VARIABLE
        std::cout << "Custom Variable in config.h: " << CUSTOM_VARIABLE << std::endl;
    #else
        std::cout << "Custom Variable is not defined in config.h." << std::endl;
    #endif
}

#endif // CONFIG_H
// my_library/library.cpp
#include "config.h"

void libraryFunction() {
    printCustomVariable();
}
// main.cpp
#include "my_library/config.h"

int main() {
    printCustomVariable();
    return 0;
}
