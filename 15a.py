#!/usr/bin/python3
import re


with open('15.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
regex = r"(\w+): \w+ (-*\d+), \w+ (-*\d+), \w+ (-*\d), \w+ (-*\d+), \w+ (-*\d+)"
ingredient = list()
for line in lines:
    m = re.match(regex, line)
    ingredient.append((m.group(1), int(m.group(2)), int(m.group(3)),
                       int(m.group(4)), int(m.group(5)), int(m.group(6))))
# print(ingredient)
best = 0
best_ratio = list()
for i in range(100):
    for j in range(100):
        for k in range(100):
            for l in range(100):
                if (i + j + k + l) == 100:
                    capacity = i * ingredient[0][1] + j * ingredient[1][1] +\
                        k * ingredient[2][1] + l * ingredient[3][1]
                    durability = i * ingredient[0][2] + j * ingredient[1][2] +\
                        k * ingredient[2][2] + l * ingredient[3][2]
                    flavor = i * ingredient[0][3] + j * ingredient[1][3] +\
                        k * ingredient[2][3] + l * ingredient[3][3]
                    texture = i * ingredient[0][4] + j * ingredient[1][4] +\
                        k * ingredient[2][4] + l * ingredient[3][4]
                    if capacity < 0:
                        capacity = 0
                    if durability < 0:
                        durability = 0
                    if flavor < 0:
                        flavor = 0
                    if texture < 0:
                        texture = 0
                    score = capacity * durability * flavor * texture
                    if score > best:
                        best = score
                        best_ratio = [i, j, k, l]
print(best, best_ratio)
