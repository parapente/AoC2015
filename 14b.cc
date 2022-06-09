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
    std::regex re("(\\w+) can fly (\\d+) km/s for (\\d+) seconds, but then must rest for (\\d+) seconds.");
    int secs = 2503;
    int maxdist;
    std::string maxrein;
    std::vector<int> rein_score;

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

    for (int i = 0; i < rein_data.size(); i++)
    {
        rein_score.push_back(0);
    }

    for (int sec = 0; sec < secs; sec++)
    {
        int cursec = sec + 1;
        std::vector<int> rein_dist;

        for (auto r : rein_data)
        {
            int remain;
            auto [name, speed, runsecs, restsecs] = r;
            int rein_runs = cursec / (runsecs + restsecs);
            if ((cursec - rein_runs * (runsecs + restsecs)) > runsecs)
            {
                remain = runsecs;
            }
            else
            {
                remain = cursec - rein_runs * (runsecs + restsecs);
            }

            rein_dist.push_back((rein_runs * runsecs + remain) * speed);
        }

        maxdist = 0;
        int i = 0;
        maxrein = "";
        auto it = max_element(std::begin(rein_dist), std::end(rein_dist));
        maxdist = *it;

        for (auto dist : rein_dist)
        {
            if (dist == maxdist)
            {
                rein_score[i]++;
            }
            i++;
        }
    }

    auto it = max_element(std::begin(rein_score), std::end(rein_score));
    std::cout << *it << std::endl;

    fin.close();
}
