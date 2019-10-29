#include <fstream>
#include <iostream>
#include <set>

void inc(std::string& curpass)
{
    int i = 7;
    int remain = 1;

    while (i > 0) {
        if (remain) {
            if (curpass[i] == 'z') {
                curpass[i] = 'a';
            }
            else {
                curpass[i] = curpass[i]+1;
                remain = 0;
            }
        }
        i--;
    }
}

bool chkpass(std::string curpass)
{
    bool stage2pass = true;
    for (char c : curpass) {
        if (c == 'i' || c == 'o' || c == 'l')
            stage2pass = false;
    }
    if (!stage2pass)
        return false;

    char cprev = 0;
    bool stage1pass = false;
    int ccount = 0;
    for (char c : curpass) {
        if ((c-cprev) == 1) {
            ccount++;
        }
        else {
            ccount = 0;
        }
        if (ccount == 2) {
            stage1pass = true;
        }
        cprev = c;
    }
    if (!stage1pass)
        return false;

    bool stage3pass = false;
    cprev = 0;
    std::set<char> pairs;
    for (char c : curpass) {
        if (c == cprev)
            pairs.insert(c);
        cprev = c;
    }
    if (pairs.size() > 1)
        stage3pass = true;
    return stage3pass;
}

std::string find_next_passwd(std::string curpass)
{
    inc(curpass);
    while (!chkpass(curpass)) {
        inc(curpass);
    }
    return curpass;
}

int main(void) {
    std::string line;
    std::ifstream fin;
    std::string curpass, nextpass;

    fin.open("11.dat");
    std::getline(fin, line);
    curpass = line;
    std::cout << "Current password: " << curpass << std::endl;
    nextpass = find_next_passwd(curpass);
    std::cout << "Next password: " << nextpass << std::endl;

    fin.close();
}
