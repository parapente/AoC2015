#!/usr/bin/python3


def step(grid):
    newgrid = [[0]*100 for x in range(100)]
    for x in range(100):
        for y in range(100):
            if grid[x][y] == '#':
                counton = 0
                for nx in [x-1, x, x+1]:
                    for ny in [y-1, y, y+1]:
                        if not (nx == x and ny == y):
                            if (nx >= 0 and ny >= 0 and nx < 100 and ny < 100):
                                if grid[nx][ny] == '#':
                                    counton += 1
                if counton in (2, 3):
                    newgrid[x][y] = '#'
                else:
                    newgrid[x][y] = '.'
            else:
                counton = 0
                for nx in [x-1, x, x+1]:
                    for ny in [y-1, y, y+1]:
                        if not (nx == x and ny == y):
                            if (nx >= 0 and ny >= 0 and nx < 100 and ny < 100):
                                if grid[nx][ny] == '#':
                                    counton += 1
                if counton == 3:
                    newgrid[x][y] = '#'
                else:
                    newgrid[x][y] = '.'
    return newgrid


with open('18.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
for i in range(100):
    lines = step(lines)
lightson = 0
for line in lines:
    lightson += line.count('#')
print(lightson)
