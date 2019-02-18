#include <fstream>
#include <iostream>

int main(void) {
    std::string line;
    std::ifstream fin;
    int floor = 0;
    int pos = 1;

    fin.open("1.dat");
    std::getline(fin, line);
    for (auto c : line) {
        if (c == '(')
            floor++;
        if (c == ')')
            floor--;
        if (floor == -1) {
            std::cout << pos << std::endl;
            break;
        }
        pos++;
    }
}
