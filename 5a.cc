#include <fstream>
#include <iostream>
#include <regex>

int main(void) {
    std::string line;
    std::ifstream fin;
    std::regex vowels("[aeiou]");
    std::regex dblletter("(.)\\1");
    std::smatch sm;
    std::string s;
    int vows;
    bool dbl;
    bool req3;
    int nice = 0;

    fin.open("5.dat");
    std::getline(fin, line);
    while(!fin.eof()) {
        s = line;
        vows = 0;
        while(std::regex_search(s, sm, vowels)) {
            vows++;
            s = sm.suffix().str();
        }
        dbl = std::regex_search(line, dblletter);
        req3 = (line.find("ab") != std::string::npos) |
                (line.find("cd") != std::string::npos) |
                (line.find("pq") != std::string::npos) |
                (line.find("xy") != std::string::npos);
        if (vows > 2 && dbl && !req3)
            nice++;
        std::getline(fin, line);
    }
    std::cout << nice << std::endl;
    fin.close();
}
