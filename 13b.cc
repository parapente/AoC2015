#include <fstream>
#include <iostream>
#include <regex>
#include <string>
#include <set>
#include <nlohmann/json.hpp>
#include <iomanip>

struct string_pair_hash
{
    std::size_t operator () (std::pair<std::string, std::string> const &v) const
    {
        return std::hash<std::string>()(v.first + v.second);
    }
};

std::vector<std::vector<std::string>> find_perms(std::vector<std::string> persons_v)
{
    std::vector<std::vector<std::string>> new_perms;

    if (persons_v.size() == 2) {
        new_perms.push_back(std::vector<std::string> {persons_v[0], persons_v[1]});
        new_perms.push_back(std::vector<std::string> {persons_v[1], persons_v[0]});
    } else {
        for (auto person : persons_v) {
            std::vector<std::string> remain = persons_v;
            std::vector<std::string>::iterator it_rem;
            for (auto it = remain.begin(); it != remain.end(); ++it) {
                if (*it == person) {
                    it_rem = it;
                    break;
                }
            }
            remain.erase(it_rem);
            auto results = find_perms(remain);
            for (auto r : results) {
                std::vector<std::string> sublist;
                sublist.push_back(person);
                sublist.insert(sublist.end(), r.begin(), r.end());
                new_perms.push_back(sublist);
            }
        }
    }
    
    return new_perms;
}

int main(void) {
    std::string line, person1, person2, status;
    int factor;
    std::ifstream fin;
    std::smatch sm;
    std::set<std::string> persons;
    std::regex re("(\\w+) would (\\w+) (\\d+) happiness units by sitting next to (\\w+).");
    std::unordered_map<
        std::pair<std::string,std::string>,
        int,
        string_pair_hash
    > dist;
    std::vector<std::string> persons_v;

    fin.open("13.dat");
    std::getline(fin, line);
    while(!fin.eof()) {
        if (std::regex_match(line, sm, re)) {
            person1 = sm[1];
            person2 = sm[4];
            status = sm[2];
            if (status == "gain") {
                factor = stol(sm[3]);
            } else {
                factor = -stol(sm[3]);
            }

            persons.emplace(person1);
            persons.emplace(person2);
            if (person1 < person2) {
                auto it = dist.find(std::make_pair(person1, person2));
                if (it != dist.end()) {
                    dist[make_pair(person1, person2)] += factor;
                } else {
                    dist[make_pair(person1, person2)] = factor;
                }
            } else {
                auto it = dist.find(std::make_pair(person2, person1));
                if (it != dist.end()) {
                    dist[make_pair(person2, person1)] += factor;
                } else {
                    dist[make_pair(person2, person1)] = factor;
                }
            }
        }
        std::getline(fin, line);
    }

    persons.emplace("Me");
    for (auto person : persons) {
        dist[make_pair(person, "Me")] = 0;
    }

    for (auto it : persons) {
        persons_v.push_back(it);
    }

    auto perms = find_perms(persons_v);

    int max_happy = -999999999;
    int total;
    std::string prev;
    std::vector<std::string> max_seats;
    for (auto item : perms) {
        total = 0;
        prev = "";

        for (auto person : item) {
            if (prev != "") {
                if (person < prev) {
                    total += dist[make_pair(person, prev)];
                } else {
                    total += dist[make_pair(prev, person)];
                }
            } else {
                if (person < item.at(item.size() - 1)) {
                    total += dist[make_pair(person, item.at(item.size() - 1))];
                } else {
                    total += dist[make_pair(item.at(item.size() - 1), person)];
                }
            }
            prev = person;
        }

        if (total > max_happy) {
            max_happy = total;
            max_seats = std::vector<std::string>(item);
        }
    }

    std::cout << "Max: " << max_happy << std::endl;

    std::cout << "Seats: ";
    for (auto it : max_seats) {
        std::cout << it << " ";
    }
    std::cout << std::endl;

    fin.close();
}
