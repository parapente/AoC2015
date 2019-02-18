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
    int paper = 0;

    fin.open("2.dat");
    while (!fin.eof()) {
        std::getline(fin, line);
        std::smatch sm;
        std::regex_match(line, sm, e);
        if (sm.size() > 0) {
            l = stoi(sm[1]);
            w = stoi(sm[2]);
            h = stoi(sm[3]);
            std::vector<int> sides{l*w, w*h, h*l};
            paper += *min_element(std::begin(sides), std::end(sides));
            for (auto el : sides) {
                paper += 2*el;
            }
        }
    }
    fin.close();
    std::cout << paper << std::endl;
}
