#!/usr/bin/python3
import re

with open('5.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
nice = 0
for word in lines:
    dbl = re.search(r"(..).*\1", word)
    dbl2 = re.search(r"(.).\1", word)
    print(dbl, dbl2)
    if dbl and dbl2:
        nice += 1
print(nice)
