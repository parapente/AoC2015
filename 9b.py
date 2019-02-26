#!/usr/bin/python3
import re


def perm(wayp):
    if len(wayp) == 1:
        return [wayp[0]]
    i = 0
    perms = list()
    while i < len(wayp):
        ret = list()
        ret = perm(wayp[0:i]+wayp[i+1:])
        j = 0
        while j < len(ret):
            if isinstance(ret[j], list):
                ret[j] = [wayp[i]] + ret[j]
            else:
                ret[j] = [wayp[i]] + [ret[j]]
            j += 1
        i += 1
        perms.extend(ret)
    # print(wayp, "-", perms)
    return perms


def calc_dist(way, dist_dic):
    i = 0
    ret = 0
    while i < (len(way) - 1):
        ret += dist_dic[(way[i], way[i+1])]
        i += 1
    return ret


with open('9.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
dist = dict()
dests = set()
for line in lines:
    tr = line[1:-1]
    m = re.match(r'(\w+) to (\w+) = (\d+)', line)
    dist[(m.group(1), m.group(2))] = int(m.group(3))
    dist[(m.group(2), m.group(1))] = int(m.group(3))
    dests.add(m.group(1))
    dests.add(m.group(2))
    print(m.group(1), "->", m.group(2), ":", m.group(3))

print('')
print(len(dests), "unique destinations:")
for d in dests:
    print(d)
print('')
print("Generating waypoints...")
waypoints = perm(list(dests))
# print(waypoints, len(waypoints))
print("Calculating distances...")
maxdist = 0
maxidx = -1
z = 0
while z < len(waypoints):
    distance = calc_dist(waypoints[z], dist)
    if distance > maxdist:
        maxdist = distance
        maxidx = z
    z += 1
print("Longest:", waypoints[maxidx], "distance:", maxdist)
