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

void permute(std::vector<std::vector<std::string>>& perm, std::vector<std::string>& usetvector, int l, int r)
{
    if (l == r) {
        std::vector<std::string> newperm(usetvector.begin(), usetvector.end());
        /*for (auto i=usetvector.begin(); i!=usetvector.end(); i++) {
            std::cout << *i << " ";
        }
        std::cout << std::endl;*/
        perm.push_back(newperm);
    }
    else {
        for (int i=l; i<=r; i++) {
            std::iter_swap(usetvector.begin()+l, usetvector.begin()+i);
            permute(perm, usetvector, l+1, r);
            std::iter_swap(usetvector.begin()+l, usetvector.begin()+i);
        }
    }
}

void find_shortest(std::vector<std::vector<std::string>> perm, std::unordered_map<std::tuple<std::string,std::string>, int, KeyHash, KeyEqual> dist)
{
    int mindist = 999999999;
    std::vector<std::string> minpath;

    for (auto p : perm) {
        int pathdist = 0;
        std::string prevnode;
        for (auto node : p) {
            int tmp;
            tmp = dist[std::make_tuple(prevnode, node)];
            if (tmp == 0)
                pathdist += dist[std::make_tuple(node, prevnode)];
            else
                pathdist += tmp;
            prevnode = node;
        }
        if (pathdist < mindist) {
            mindist = pathdist;
            minpath = p;
        }
    }
    std::cout << "Path with minimum distance: ";
    for (auto n : minpath)
        std::cout << n << " ";
    std::cout << ": " << mindist << std::endl;
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
    std::vector<std::string> usetvector(uset.begin(), uset.end());

    std::cout << std::endl << uset.size() << " unique destinations" << std::endl;

    permute(perm, usetvector, 0, usetvector.size()-1);
    //std::cout << perm.size() << std::endl;
    find_shortest(perm, dist);
    fin.close();
}
