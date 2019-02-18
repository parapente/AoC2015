#include <fstream>
#include <iostream>

int main(void) {
    std::string line;
    std::ifstream fin;
    int floor = 0;

    fin.open("1.dat");
    std::getline(fin, line);
    for (auto c : line) {
        if (c == '(')
            floor++;
        if (c == ')')
            floor--;
    }
    std::cout << floor << std::endl;
}
