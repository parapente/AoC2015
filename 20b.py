#!/usr/bin/python3
import math
import itertools
import sys


def primeFactors(n):
    result = list()
    while n % 2 == 0:
        result.append(2)
        n = n // 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            result.append(i)
            n = n // i

    if n > 2:
        result.append(n)
    return result


def main():
    with open('20.dat') as f:
        data = f.read()
    lines = data.split('\n')
    lines.pop()
    maxpresents = int(lines[0])
    counter = dict()

    house = 1
    housepresents = 0
    while housepresents < maxpresents:
        primes = primeFactors(house)
        elves = set()
        elves.add(1)
        for i, _ in enumerate(primes):
            if i == 0:
                elves.update(primes)
            else:
                c = set(itertools.combinations(primes, i+1))
                # print('Comb:', c, 'i:', i+1)
                for e in c:
                    prod = 1
                    for num in e:
                        prod *= num
                    elves.add(prod)
        # print(house, primes)
        # print(elves)
        presents = 0
        for e in elves:
            if e not in counter:
                counter[e] = 0
            counter[e] += 1
            if counter[e] <= 50:
                presents += e * 11
        if presents > maxpresents:
            print('House:', house, 'presents:', presents, 'elves:', elves)
            sys.exit(0)
        house += 1


if __name__ == "__main__":
    main()
