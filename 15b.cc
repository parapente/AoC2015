#include <fstream>
#include <iostream>
#include <regex>
#include <string>

int main(void)
{
    std::string line;
    std::ifstream fin;
    std::smatch sm;
    std::vector<std::tuple<std::string, int, int, int, int, int>>
        ingredient;
    std::regex re("(\\w+): \\w+ (-*\\d+), \\w+ (-*\\d+), \\w+ (-*\\d), \\w+ (-*\\d+), \\w+ (-*\\d+)");

    fin.open("15.dat");
    std::getline(fin, line);
    while (!fin.eof())
    {
        if (std::regex_match(line, sm, re))
        {
            ingredient.push_back(
                std::make_tuple(sm[1],
                                std::stoi(sm[2]),
                                std::stoi(sm[3]),
                                std::stoi(sm[4]),
                                std::stoi(sm[5]),
                                std::stoi(sm[6])));
        }
        std::getline(fin, line);
    }

    long best = 0;

    std::array<long, 4> best_ratio;
    for (int i = 0; i < 100; i++)
        for (int j = 0; j < 100; j++)
            for (int k = 0; k < 100; k++)
                for (int l = 0; l < 100; l++)
                    if ((i + j + k + l) == 100)
                    {
                        long capacity = i * std::get<1>(ingredient[0]) + j * std::get<1>(ingredient[1]) +
                                        k * std::get<1>(ingredient[2]) + l * std::get<1>(ingredient[3]);
                        long durability = i * std::get<2>(ingredient[0]) + j * std::get<2>(ingredient[1]) +
                                          k * std::get<2>(ingredient[2]) + l * std::get<2>(ingredient[3]);
                        long flavor = i * std::get<3>(ingredient[0]) + j * std::get<3>(ingredient[1]) +
                                      k * std::get<3>(ingredient[2]) + l * std::get<3>(ingredient[3]);
                        long texture = i * std::get<4>(ingredient[0]) + j * std::get<4>(ingredient[1]) +
                                       k * std::get<4>(ingredient[2]) + l * std::get<4>(ingredient[3]);
                        long calories = i * std::get<5>(ingredient[0]) + j * std::get<5>(ingredient[1]) +
                                        k * std::get<5>(ingredient[2]) + l * std::get<5>(ingredient[3]);
                        if (capacity < 0)
                            capacity = 0;
                        if (durability < 0)
                            durability = 0;
                        if (flavor < 0)
                            flavor = 0;
                        if (texture < 0)
                            texture = 0;
                        long score = capacity * durability * flavor * texture;
                        if (calories == 500 && score > best)
                        {
                            best = score;
                            best_ratio = {i, j, k, l};
                        }
                    }
    std::cout << best << " [ ";
    for (auto item : best_ratio)
    {
        std::cout << item << ' ';
    }
    std::cout << ']' << std::endl;

    fin.close();
}
