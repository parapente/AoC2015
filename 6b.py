#!/usr/bin/python3
import re

with open('6.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
grid = [[0] * 1000 for i in range(1000)]
for line in lines:
    m = re.match(r"(^.+) (\d+),(\d+) through (\d+),(\d+)", line)
    cmd = m.group(1)
    x1, y1, x2, y2 = int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
    if cmd == "turn on":
        x = x1
        while x <= x2:
            y = y1
            while y <= y2:
                grid[x][y] += 1
                y += 1
            x += 1
    if cmd == "turn off":
        x = x1
        while x <= x2:
            y = y1
            while y <= y2:
                if grid[x][y] > 0:
                    grid[x][y] -= 1
                y += 1
            x += 1
    if cmd == "toggle":
        x = x1
        while x <= x2:
            y = y1
            while y <= y2:
                grid[x][y] += 2
                y += 1
            x += 1
count = 0
x = 0
while x < 1000:
    y = 0
    while y < 1000:
        count += grid[x][y]
        y += 1
    x += 1
print(count)
