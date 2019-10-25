#!/usr/bin/python3


def readnum(n):
    prev = ''
    count = 0
    newnum = ''
    for c in n:
        if prev == '':
            prev = c
            count = 1
        elif prev == c:
            count += 1
        else:
            newnum += str(count)+prev
            prev = c
            count = 1
    newnum += str(count)+prev
    return newnum


with open('10.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
num = lines[0]
for x in range(50):
    nextnum = readnum(num)
    num = nextnum
print(len(num))
