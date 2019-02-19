#include <fstream>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <openssl/md5.h>

int main(void) {
    std::string line;
    std::string tmp;
    std::ifstream fin;
    unsigned char hash[MD5_DIGEST_LENGTH];
    int i;
    int len;
    bool done;

    fin.open("4.dat");
    std::getline(fin, line);
    i = 1;
    done = false;
    do {
        tmp = line + std::to_string(i);
        len = tmp.length();
        MD5((const unsigned char *)tmp.data(), len, hash);
        std::ostringstream sstr;
        sstr << std::hex << std::setfill('0');
        for (long long c: hash)
        {
            sstr << std::setw(2) << (long long) c;
        }
        if (sstr.str().substr(0,5) == std::string("00000"))
            done = true;
        /* std::cout << sstr.str().substr(0,5) << " - " << sstr.str() << " - " << i << std::endl; */
        i++;
    } while (!done);
    std::cout << i-1 << std::endl;
    fin.close();
}
