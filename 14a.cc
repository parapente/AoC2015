#include <fstream>
#include <iostream>
#include <regex>
#include <string>

int main(void)
{
    std::string line;
    std::ifstream fin;
    std::smatch sm;
    std::vector<std::tuple<std::string, int, int, int>> rein_data;
    std::vector<int> rein_dist;
    std::regex re("(\\w+) can fly (\\d+) km/s for (\\d+) seconds, but then must rest for (\\d+) seconds.");
    int secs = 2503;

    fin.open("14.dat");
    std::getline(fin, line);
    while (!fin.eof())
    {
        if (std::regex_match(line, sm, re))
        {
            rein_data.push_back(std::make_tuple(sm[1], std::stoi(sm[2]), std::stoi(sm[3]), std::stoi(sm[4])));
        }
        std::getline(fin, line);
    }

    for (auto r : rein_data)
    {
        int remain;
        auto [name, speed, runsecs, restsecs] = r;
        int rein_runs = secs / (runsecs + restsecs);
        if ((secs - rein_runs * (runsecs + restsecs)) > runsecs)
        {
            remain = runsecs;
        }
        else
        {
            remain = secs - rein_runs * (runsecs + restsecs);
        }

        rein_dist.push_back((rein_runs * runsecs + remain) * speed);
    }

    int maxdist = 0;
    int i = 0;
    std::string maxrein = "";
    for (auto el : rein_data)
    {
        if (maxdist < rein_dist[i])
        {
            maxdist = rein_dist[i];
            maxrein = std::get<0>(el);
        }
        i++;
    }

    std::cout << maxrein << ' ' << maxdist << std::endl;

    fin.close();
}
