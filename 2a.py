#!/usr/bin/python3

with open('2.dat') as f:
    data = f.read()
presents = data.split('\n')
presents.pop()  # Remove last empty line
paper = 0
for p in presents:
    l, w, h = p.split('x')
    l, w, h = int(l), int(w), int(h)
    sides = [l*w, w*h, h*l]
    mside = min(sides)
    area = sum([2*i for i in sides])
    paper += area + mside
print(paper)
