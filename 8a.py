#!/usr/bin/python3
import re

with open('8.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
total = 0
for line in lines:
    tr = line[1:-1]
    matches = re.findall(r'\\x[0-9a-f]{2}', line)
    for m in matches:
        tr = tr.replace(m, chr(int("0"+m[1:4], 16)))
    tr = tr.replace("\\\\", "\\")
    tr = tr.replace("\\\"", "\"")
    # print(len(line), len(tr), line)
    total += len(line) - len(tr)
print(total)
