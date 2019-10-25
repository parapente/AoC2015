#include <fstream>
#include <iostream>

std::string readnum(std::string num) {
    char prev = 0;
    int count = 0;
    std::string newnum;

    for (char c : num) {
        if (prev == 0) {
            prev = c;
            count = 1;
        }
        else if (prev == c) {
            count++;
        }
        else {
            newnum += std::to_string(count) + std::string(1, prev);
            prev = c;
            count = 1;
        }
    }
    newnum += std::to_string(count) + std::string(1, prev);
    return(newnum);
}

int main(void) {
    std::string line;
    std::ifstream fin;
    std::string num, nextnum;

    fin.open("10.dat");
    std::getline(fin, line);
    num = line;
    for(int i=0; i<50; i++) {
        nextnum = readnum(num);
        num = nextnum;
    }
    std::cout << num << std::endl;
    std::cout << num.size() << std::endl;

    fin.close();
}
