#!/usr/bin/python3

with open('8.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
total = 0
for line in lines:
    tr = line.replace("\\", "\\\\")
    tr = tr.replace("\"", "\\\"")
    tr = '"' + tr + '"'
    # print(len(line), len(tr), line, tr)
    total += len(tr) - len(line)
print(total)
