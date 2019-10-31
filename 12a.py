#!/usr/bin/python3
import re

with open('12.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
for line in lines:
    m = re.findall(r"(-*\d+)", line)
    nums = [int(x) for x in m]
    sumofnums = sum(nums)
print(sumofnums)
