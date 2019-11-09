#!/usr/bin/python3
import re


def find_perms(objs):
    # print(objs)
    newperms = list()
    if len(objs) == 2:
        newperms = [[objs[0], objs[1]], [objs[1], objs[0]]]
    else:
        for obj in objs:
            remain = list(objs)
            remain.remove(obj)
            results = find_perms(remain)
            for r in results:
                sublist = [obj]
                sublist.extend(r)
                newperms.append(sublist)
    return newperms


with open('13.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
dist = dict()
persons = set()
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
    persons.add(person1)
    persons.add(person2)
    if person1 < person2:
        if (person1, person2) in dist:
            dist[(person1, person2)] += factor
        else:
            dist[(person1, person2)] = factor
    else:
        if (person2, person1) in dist:
            dist[(person2, person1)] += factor
        else:
            dist[(person2, person1)] = factor

# Add myself
persons.add('Me')
for p in persons:
    dist[(p, 'Me')] = 0

distc = dict(dist)
for k, v in distc.items():
    (key1, key2) = k
    dist[(key2, key1)] = v

# for k, v in dist.items():
#     print(k)
#     print(v)
perms = find_perms(list(persons))
# print(perms)
maxhappy = -99999999
maxseats = list()
for item in perms:
    total = 0
    prev = ''
    for person in item:
        if prev != '':
            total += dist[(person, prev)]
        else:
            total += dist[(person, item[len(item)-1])]
        prev = person
    if total > maxhappy:
        maxhappy = total
        maxseats = list(item)
        # print(maxhappy)
        # print(maxseats)
print('Max: ', maxhappy)
print('Seats: ', maxseats)
