#include <fstream>
#include <iostream>
#include <vector>
#include <deque>
#include <regex>
#include <unordered_map>
#include <unordered_set>
#include <tuple>

struct KeyHash {
    std::size_t operator()(const std::tuple<std::string, std::string>& k) const
    {
        return std::hash<std::string>()(std::get<0>(k) + std::get<1>(k));
    }
};

struct KeyEqual {
    bool operator()(const std::tuple<std::string, std::string>& lhs,
                    const std::tuple<std::string, std::string>& rhs) const
    {
        return std::get<0>(lhs) == std::get<0>(rhs) &&
               std::get<1>(lhs) == std::get<1>(rhs);
    }
};

void find_perm(std::vector<std::vector<std::string>>& perm, std::unordered_set<std::string>& uset) {

}

int main(void) {
    std::string line;
    std::ifstream fin;
    std::vector<std::vector<std::string>> perm;
    std::string tmp;
    std::smatch sm;
    std::regex re("(\\w+) to (\\w+) = (\\d+)");
    std::unordered_map<std::tuple<std::string,std::string>, int, KeyHash, KeyEqual> dist;
    std::unordered_set<std::string> uset;

    fin.open("9.dat");
    std::getline(fin, line);
    while(!fin.eof()) {
        if (std::regex_match(line, sm, re)) {
            dist[std::make_tuple(sm[1], sm[2])] = stol(sm[3]);
            dist[std::make_tuple(sm[2], sm[1])] = stol(sm[3]);
        }
        uset.emplace(sm[1]);
        uset.emplace(sm[2]);
        std::cout << sm[1] << " -> " << sm[2] << " = " << sm[3] << std::endl;
        std::getline(fin, line);
    }

    std::cout << std::endl << uset.size() << " unique destinations" << std::endl;

    find_perm(perm, uset);
    /* for (auto cmd : dq) { */
    /*     for (auto op : cmd) { */
    /*         std::cout << op << " "; */
    /*     } */
    /*     std::cout << std::endl; */
    /* } */

    /* while (dq.size()) { */
    /*     std::vector<std::string> cmd; */
    /*     cmd = dq.front(); */
    /*     dq.pop_front(); */
    /* } */
    fin.close();
}
