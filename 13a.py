#!/usr/bin/python3
import re

with open('13.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
for line in lines:
    m = re.match(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)", line)
    person1 = m.group(1)
    person2 = m.group(4)
    status = m.group(2)
    factor = m.group(3)
    if status == "gain":
        factor = int(factor)
    else:
        factor = -int(factor)
    print(person1+"->"+person2+" "+str(factor))


