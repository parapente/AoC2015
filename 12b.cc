#include <fstream>
#include <iostream>
#include <regex>
#include <string>
#include <nlohmann/json.hpp>
#include <iomanip>

using json = nlohmann::json;

int dosum(json jobj) {
    int subtotal = 0;
    std::vector<json> jlist;

    for (auto& el : jobj.items()) {
        if (el.value().is_number()) {
            subtotal += el.value().get<int>();
        }
        if (el.value().is_string() && (el.value().get<std::string>() == "red") && jobj.is_object())
            return 0;
        if (el.value().is_structured()) {
            jlist.push_back(el.value());
        }
    }
    for (auto i : jlist) {
        subtotal += dosum(i);
    }
    return subtotal;
}

int main(void) {
    std::string line;
    std::ifstream fin;
    std::smatch sm;
    std::regex re("(-*\\d+)");
    int total = 0;

    fin.open("12.dat");
    std::getline(fin, line);
    json j_complete;
    while(!fin.eof()) {
        j_complete = json::parse(line.begin(), line.end());
        /* std::cout << std::setw(4) << j_complete << std::endl; */
        std::getline(fin, line);
    }
    total = dosum(j_complete);
    std::cout << "Total: " << total << std::endl;
    fin.close();
}
