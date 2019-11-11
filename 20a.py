#!/usr/bin/python3
import math

def primeFactors(n):
    result = list()
    while n % 2 == 0:
        result.append(2)
        n = n // 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            result.append(i)
            n = n // i

    if n > 2:
        result.append(n)
    return result


with open('20.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
maxpresents = int(lines[0])

house = 1
housepresents = 0
while housepresents < maxpresents:
    elves = primeFactors(house)
    print(house, elves)
    house += 1
