#!/usr/bin/python3
import re
import sys
import blist


def findsol(mol, target, steps, maxlen, replacements):
    branches = [(mol, steps)]
    # print(branches)
    index = blist.sorteddict()
    i = 0
    solution = -1
    while branches:
        i += 1
        # print(branch)
        if i % 100000 == 0:
            print(len(index), len(branches), end='\r')
        branch = branches.pop()
        steps = branch[1] + 1
        # if i == 500000:
        #     for key, val in index.items():
        #         print(key, val)
        # If no other branch reached here first
        if branch[0] not in index or (index[branch[0]] > branch[1]):
            index[branch[0]] = branch[1]
            for rep in replacements:
                done = False
                off = 0
                while not done:
                    done = True
                    pos = branch[0].find(rep[1], off)
                    # print(rep)
                    # If found
                    if pos != -1:
                        done = False
                        newmol = branch[0][:pos] + rep[0] +\
                            branch[0][pos+len(rep[1]):]
                        if newmol == target:
                            # print('Target reached in', steps, 'steps!')
                            if solution == -1 or solution > steps:
                                solution = steps
                                print('Solution:', solution)
                                sys.exit(0)
                        else:
                            if rep[0] != 'e':
                                branches.append((newmol, steps))
                        off = pos + len(rep[1])
                # print(branches)
                # input()
    return solution


def main():
    with open('19.dat') as f:
        data = f.read()
    lines = data.split('\n')
    lines.pop()
    targetmolecule = str(lines.pop())
    lines.pop()
    replacements = list()
    for line in lines:
        m = re.match(r"(\w+) => (\w+)", line)
        replacements.append((m.group(1), m.group(2)))
    replacements.sort(key=lambda x: x[1])
    # print(replacements)
    # print(len(targetmolecule))
    steps = 0
    molecule = 'e'
    minsol = findsol(targetmolecule, molecule, steps, len(targetmolecule),
                     replacements)
    print(minsol)


if __name__ == "__main__":
    main()
