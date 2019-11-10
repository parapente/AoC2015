#!/usr/bin/python3
import re

ticket = [('children', 3), ('cats', 7), ('samoyeds', 2), ('pomeranians', 3),
          ('akitas', 0), ('vizslas', 0), ('goldfish', 5), ('trees', 3),
          ('cars', 2), ('perfumes', 1)]
with open('16.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
regex = r".*: (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)"
sue = list()
sue_score = [0] * 500
for line in lines:
    m = re.match(regex, line)
    sue.append([(m.group(1), int(m.group(2))),
                (m.group(3), int(m.group(4))),
                (m.group(5), int(m.group(6)))])
for item in ticket:
    for i in range(500):
        score = sue_score[i]
        for clue in sue[i]:
            # print(clue, item)
            if clue == item:
                score += 1
        sue_score[i] = score
maxscore = max(sue_score)
# print(sue_score)
print('Sue: ', str(sue_score.index(maxscore) + 1))
