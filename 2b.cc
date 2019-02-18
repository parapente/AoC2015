#include <fstream>
#include <iostream>
#include <regex>
#include <algorithm>
#include <vector>

int main(void) {
    std::string line;
    std::ifstream fin;
    std::regex e("(\\d+)x(\\d+)x(\\d+)");
    int l, w, h;
    int ribbon = 0;

    fin.open("2.dat");
    while (!fin.eof()) {
        std::getline(fin, line);
        std::smatch sm;
        std::regex_match(line, sm, e);
        if (sm.size() > 0) {
            l = stoi(sm[1]);
            w = stoi(sm[2]);
            h = stoi(sm[3]);
            std::vector<int> sides{2*l+2*w, 2*w+2*h, 2*h+2*l};
            ribbon += *min_element(std::begin(sides), std::end(sides)) + l*w*h;
        }
    }
    fin.close();
    std::cout << ribbon << std::endl;
}
