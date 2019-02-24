#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <regex>
#include <cstdlib>

void replaceAll(std::string& str, const std::string& from, const std::string& to) {
    if(from.empty())
        return;
    size_t start_pos = 0;
    while((start_pos = str.find(from, start_pos)) != std::string::npos) {
        str.replace(start_pos, from.length(), to);
        start_pos += to.length(); // In case 'to' contains 'from', like replacing 'x' with 'yx'
    }
}

int main(void) {
    std::string line;
    std::string tmp;
    std::ifstream fin;
    std::stringstream sstream;
    int total = 0;

    fin.open("8.dat");
    std::getline(fin, line);
    while(!fin.eof()) {
        /* std::cout << line << " -> "; */
        total -= line.length();
        replaceAll(line, std::string("\\"), std::string("\\\\"));
        replaceAll(line, std::string("\""), std::string("\\\""));
        line = std::string("\"") + line + std::string("\"");
        total += line.length();
        /* std::cout << line << std::endl; */
        std::getline(fin, line);
    }
    fin.close();
    std::cout << total << std::endl;
}
