#include <fstream>
#include <iostream>
#include <regex>
#include <string>

int main(void) {
    std::string line;
    std::ifstream fin;
    std::smatch sm;
    std::regex re("(-*\\d+)");
    int total = 0;

    fin.open("12.dat");
    std::getline(fin, line);
    while(!fin.eof()) {
        std::string::const_iterator searchStart( line.cbegin() );
        while(std::regex_search(searchStart, line.cend(), sm, re)) {
                std::cout << sm[0] << " + ";
                total += std::stoi(sm[0]);
                searchStart = sm.suffix().first;
        }
        std::cout << std::endl;
        std::getline(fin, line);
    }
    std::cout << "Total: " << total << std::endl;
    fin.close();
}
