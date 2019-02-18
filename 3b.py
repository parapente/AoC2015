#!/usr/bin/python3

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0


with open('3.dat') as f:
    data = f.read()
house = dict()
house[(0, 0)] = 1
i = 0
x = 0
y = 0
santa = Point()
robosanta = Point()
for c in data:
    if c == '>':
        if i % 2 == 0:
            santa.x += 1
        else:
            robosanta.x += 1
    if c == '<':
        if i % 2 == 0:
            santa.x -= 1
        else:
            robosanta.x -= 1
    if c == '^':
        if i % 2 == 0:
            santa.y += 1
        else:
            robosanta.y += 1
    if c == 'v':
        if i % 2 == 0:
            santa.y -= 1
        else:
            robosanta.y -= 1
    if i % 2 == 0:
        x = santa.x
        y = santa.y
    else:
        x = robosanta.x
        y = robosanta.y
    if (x, y) in house:
        house[(x, y)] += 1
    else:
        house[(x, y)] = 1
    i += 1
print(len(house))
