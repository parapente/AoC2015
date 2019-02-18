#!/usr/bin/python3

with open('3.dat') as f:
    data = f.read()
house = dict()
x = 0
y = 0
for c in data:
    if c == '>':
        x += 1
    if c == '<':
        x -= 1
    if c == '^':
        y += 1
    if c == 'v':
        y -= 1
    if (x, y) in house:
        house[(x, y)] += 1
    else:
        house[(x, y)] = 1
print(len(house))
