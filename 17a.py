#!/usr/bin/python3


def find_comb(cont, quant):
    if len(cont) == 1:
        if cont[0][0] == quant:
            return cont
        return False
    solutions = list()
    for item in cont:
        newquant = quant - item[0]
        if newquant == 0:
            solutions.append([item])
        elif newquant > 0:
            newcont = list(cont)
            newcont.remove(item)
            result = find_comb(newcont, newquant)
            if result:
                for i in result:
                    newitem = [item]
                    newitem.extend(i)
                    solutions.append(newitem)
    if not solutions:
        return False
    return solutions


with open('17.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
container = [(int(x), i) for i, x in enumerate(lines)]
container.sort(reverse=True)
# print(container)
combinations = find_comb(container, 150)
for sol in combinations:
    sol.sort()
combinations.sort()
# print(combinations)
dedup = [val for key, val in enumerate(combinations)
         if key == 0 or combinations[key] != combinations[key - 1]]
print(len(dedup))
