#!/usr/bin/python3

with open('2.dat') as f:
    data = f.read()
presents = data.split('\n')
presents.pop()  # Remove last empty line
ribbon = 0
for p in presents:
    l, w, h = p.split('x')
    l, w, h = int(l), int(w), int(h)
    sides = [2*l+2*w, 2*w+2*h, 2*h+2*l]
    mside = min(sides)
    ribbon += mside + l*w*h
print(ribbon)
