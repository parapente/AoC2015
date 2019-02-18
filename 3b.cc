#include <fstream>
#include <iostream>
#include <utility>
#include <map>

class Point {
    public:
        int x;
        int y;
        Point() : x {0}, y {0} {}
};

int main(void) {
    std::string line;
    std::ifstream fin;
    int x = 0;
    int y = 0;
    int i = 0;
    Point santa;
    Point robosanta;
    Point *santa_ptr;
    std::map<std::pair<int,int>,int> house;

    fin.open("3.dat");
    std::getline(fin, line);
    house[std::make_pair(0,0)] = 1;
    for (auto c : line) {
        if ((i % 2) == 0)
            santa_ptr = &santa;
        else
            santa_ptr = &robosanta;
        switch(c) {
            case '>':
                santa_ptr->x++;
                break;
            case '<':
                santa_ptr->x--;
                break;
            case '^':
                santa_ptr->y++;
                break;
            case 'v':
                santa_ptr->y--;
        }
        x = santa_ptr->x;
        y = santa_ptr->y;
        if (house.count(std::make_pair(x,y)))
            house[std::make_pair(x,y)]++;
        else
            house[std::make_pair(x,y)] = 1;
        i++;
    }
    fin.close();
    std::cout << house.size() << std::endl;
}
