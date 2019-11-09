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
rein_score = [0]*len(rein_data)
for sec in range(secs):
    cursec = sec + 1
    reindist = list()
    for r in rein_data:
        (name, speed, runsecs, restsecs) = r
        reinruns = cursec // (runsecs + restsecs)
        if (cursec - reinruns * (runsecs + restsecs)) > runsecs:
            remain = runsecs
        else:
            remain = cursec - reinruns * (runsecs + restsecs)
        reindist.append((reinruns * runsecs + remain) * speed)

    maxdist = max(reindist)
    for i, dist in enumerate(reindist):
        if dist == maxdist:
            rein_score[i] += 1
print(max(rein_score))
