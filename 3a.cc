#include <fstream>
#include <iostream>
#include <utility>
#include <map>

int main(void) {
    std::string line;
    std::ifstream fin;
    int x = 0;
    int y = 0;
    std::map<std::pair<int,int>,int> house;

    fin.open("3.dat");
    std::getline(fin, line);
    for (auto c : line) {
        switch(c) {
            case '>':
                x++;
                break;
            case '<':
                x--;
                break;
            case '^':
                y++;
                break;
            case 'v':
                y--;
        }
        if (house.count(std::make_pair(x,y)))
            house[std::make_pair(x,y)]++;
        else
            house[std::make_pair(x,y)] = 1;

    }
    fin.close();
    std::cout << house.size() << std::endl;
}
