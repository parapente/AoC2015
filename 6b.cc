#include <fstream>
#include <iostream>
#include <regex>

int main(void) {
    std::string line;
    std::ifstream fin;
    std::regex re("(^.+) (\\d+),(\\d+) through (\\d+),(\\d+)");
    std::smatch sm;
    std::string s;
    std::string cmd;
    int x1, y1, x2, y2;
    int grid[1000][1000];
    int cnt = 0;

    fin.open("6.dat");
    std::getline(fin, line);
    for (int x=0; x<1000; x++) {
        for (int y=0; y<1000; y++) {
            grid[x][y] = 0;
        }
    }
    while(!fin.eof()) {
        s = line;
        std::regex_match(s, sm, re);
        cmd = sm[1];
        x1 = stoi(sm[2]);
        y1 = stoi(sm[3]);
        x2 = stoi(sm[4]);
        y2 = stoi(sm[5]);
        /* std::cout << cmd << " : " << x1 << "," << y1 << " - " << x2 << "," << y2 << std::endl; */
        if (cmd == "turn on") {
            for (int x=x1; x<=x2; x++) {
                for (int y=y1; y<=y2; y++) {
                    grid[x][y]++;
                }
            }
        }
        else if (cmd == "turn off") {
            for (int x=x1; x<=x2; x++) {
                for (int y=y1; y<=y2; y++) {
                    if (grid[x][y] > 0)
                        grid[x][y]--;
                }
            }
        }
        else {
            for (int x=x1; x<=x2; x++) {
                for (int y=y1; y<=y2; y++) {
                    grid[x][y] += 2;
                }
            }
        }
        std::getline(fin, line);
    }
    for (int x=0; x<1000; x++) {
        for (int y=0; y<1000; y++) {
                cnt += grid[x][y];
        }
    }
    std::cout << cnt << std::endl;
    fin.close();
}
