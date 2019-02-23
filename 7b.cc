#include <fstream>
#include <iostream>
#include <unordered_map>
#include <exception>
#include <vector>
#include <deque>
#include <sstream>

bool is_number(const std::string& s) {
    return !s.empty() && s.find_first_not_of("0123456789") == std::string::npos;
}

int iget(std::string& s, std::unordered_map<std::string, int>& val) {
    if (is_number(s))
        return stoi(s);
    else
        return val.at(s);
}

void op_set(std::vector<std::string>& cmd, std::unordered_map<std::string, int>& val) {
    val[cmd[2]] = iget(cmd[0], val);
}

void op_not(std::vector<std::string>& cmd, std::unordered_map<std::string, int>& val) {
    val[cmd[3]] = ~iget(cmd[1], val);
}

void op_and(std::vector<std::string>& cmd, std::unordered_map<std::string, int>& val) {
    val[cmd[4]] = iget(cmd[0], val) & iget(cmd[2], val);
}

void op_or(std::vector<std::string>& cmd, std::unordered_map<std::string, int>& val) {
    val[cmd[4]] = iget(cmd[0], val) | iget(cmd[2], val);
}

void op_lshift(std::vector<std::string>& cmd, std::unordered_map<std::string, int>& val) {
    val[cmd[4]] = iget(cmd[0], val) << iget(cmd[2], val);
}

void op_rshift(std::vector<std::string>& cmd, std::unordered_map<std::string, int>& val) {
    val[cmd[4]] = iget(cmd[0], val) >> iget(cmd[2], val);
}

int main(void) {
    std::string line;
    std::ifstream fin;
    std::deque<std::vector<std::string>> dq;
    std::string tmp;
    std::unordered_map<std::string, int> val;

    fin.open("7.dat");
    std::getline(fin, line);
    while(!fin.eof()) {
        std::stringstream check(line);
        std::vector<std::string> tokens;

        while (getline(check, tmp, ' ')) {
            tokens.push_back(tmp);
        }
        dq.push_back(tokens);
        std::getline(fin, line);
    }

    /* for (auto cmd : dq) { */
    /*     for (auto op : cmd) { */
    /*         std::cout << op << " "; */
    /*     } */
    /*     std::cout << std::endl; */
    /* } */

    while (dq.size()) {
        std::vector<std::string> cmd;
        cmd = dq.front();
        dq.pop_front();
        try {
            /* std::cerr << "Trying: "; */
            /* for (auto op : cmd) { */
            /*     std::cerr << op << " "; */
            /* } */
            /* std::cerr << std::endl; */
            if (cmd[1] == "->")
                op_set(cmd, val);
            if (cmd[0] == "NOT")
                op_not(cmd, val);
            if (cmd[1] == "AND")
                op_and(cmd, val);
            if (cmd[1] == "OR")
                op_or(cmd, val);
            if (cmd[1] == "LSHIFT")
                op_lshift(cmd, val);
            if (cmd[1] == "RSHIFT")
                op_rshift(cmd, val);
        }
        catch(std::out_of_range e) {
            /* std::cerr << "KeyError!" << std::endl; */
            dq.push_back(cmd);
        }
    }
    std::cout << val["a"] << std::endl;

    // Second phase
    int aval;
    aval = val["a"];
    val.clear();
    val["b"] = aval;

    fin.clear();
    fin.seekg(0);
    std::getline(fin, line);
    while(!fin.eof()) {
        std::stringstream check(line);
        std::vector<std::string> tokens;

        while (getline(check, tmp, ' ')) {
            tokens.push_back(tmp);
        }
        dq.push_back(tokens);
        std::getline(fin, line);
    }
    /* std::cerr << "File reread" << std::endl; */

    while (dq.size()) {
        std::vector<std::string> cmd;
        cmd = dq.front();
        dq.pop_front();
        try {
            /* std::cerr << "Trying: "; */
            /* for (auto op : cmd) { */
            /*     std::cerr << op << " "; */
            /* } */
            /* std::cerr << std::endl; */
            if (cmd[1] == "->") {
                if (cmd[2] == "b") {
                    /* std::cerr << "Overriding b" << std::endl; */
                    continue;
                }
                op_set(cmd, val);
            }
            if (cmd[0] == "NOT")
                op_not(cmd, val);
            if (cmd[1] == "AND")
                op_and(cmd, val);
            if (cmd[1] == "OR")
                op_or(cmd, val);
            if (cmd[1] == "LSHIFT")
                op_lshift(cmd, val);
            if (cmd[1] == "RSHIFT")
                op_rshift(cmd, val);
        }
        catch(std::out_of_range e) {
            /* std::cerr << "KeyError!" << std::endl; */
            dq.push_back(cmd);
        }
    }
    fin.close();
    std::cout << val["a"] << std::endl;
}
