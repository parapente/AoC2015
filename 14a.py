#!/usr/bin/python3
import re


with open('14.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
secs = 2503
regex = r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
rein_data = list()
for line in lines:
    m = re.match(regex, line)
    rein_data.append((m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4))))
reindist = list()
for r in rein_data:
    (name, speed, runsecs, restsecs) = r
    reinruns = secs // (runsecs + restsecs)
    if (secs - reinruns * (runsecs + restsecs)) > runsecs:
        remain = runsecs
    else:
        remain = secs - reinruns * (runsecs + restsecs)
    reindist.append((reinruns * runsecs + remain) * speed)

maxdist = 0
maxrein = ''
for i, el in enumerate(rein_data):
    # print(el[0]+' '+str(reindist[i]))
    if maxdist < reindist[i]:
        maxdist = reindist[i]
        maxrein = el[0]
print(maxrein+' '+str(maxdist))
