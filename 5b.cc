#include <fstream>
#include <iostream>
#include <regex>

int main(void) {
    std::string line;
    std::ifstream fin;
    std::regex dblletter("(..).*\\1");
    std::regex dblletter2("(.).\\1");
    std::smatch sm;
    std::string s;
    bool dbl;
    bool dbl2;
    int nice = 0;

    fin.open("5.dat");
    std::getline(fin, line);
    while(!fin.eof()) {
        s = line;
        dbl = std::regex_search(line, dblletter);
        dbl2 = std::regex_search(line, dblletter2);
        if (dbl && dbl2)
            nice++;
        std::getline(fin, line);
    }
    std::cout << nice << std::endl;
    fin.close();
}
