#!/usr/bin/python3
import re

with open('5.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
nice = 0
for word in lines:
    vows = len(re.findall('[aeiou]', word))
    dbl = re.search(r"(.)\1", word)
    req3 = False
    for x in ["ab", "cd", "pq", "xy"]:
        req3 = req3 or x in word
    if dbl is None:
        print(vows, 0, req3)
    else:
        print(vows, len(dbl.groups()), req3)
    if vows > 2 and dbl and not req3:
        nice += 1
print(nice)
