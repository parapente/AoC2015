#!/usr/bin/python3
import re


with open('19.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
molecule = str(lines.pop())
lines.pop()
replacements = list()
for line in lines:
    m = re.match(r"(\w+) => (\w+)", line)
    replacements.append((m.group(1), m.group(2)))
print(replacements)
mols = set()
for replacement in replacements:
    i = 0
    idx = molecule.find(replacement[0], i)
    while idx != -1:
        newmol = molecule[0:i] + molecule[i:].replace(replacement[0],
                                                      replacement[1], 1)
        mols.add(newmol)
        i = idx + 1
        idx = molecule.find(replacement[0], i)
print(len(mols))
