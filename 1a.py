#!/usr/bin/python3

with open('1.dat') as f:
    data = f.read()
floor = 0
for char in data:
    if char == '(':
        floor += 1
    if char == ')':
        floor -= 1
print(floor)
