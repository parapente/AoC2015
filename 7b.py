#!/usr/bin/python3
from collections import deque

with open('7.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
dq = deque()
val = dict()
for cmd in lines:
    ops = list()
    ops = cmd.split(' ')
    dq.append(ops)

while dq:
    op = list()
    op = dq.popleft()
    try:
        # print('Trying', op)
        if op[1] == '->':
            if op[0].isdigit():
                val[op[2]] = int(op[0])
            else:
                val[op[2]] = val[op[0]]
        if op[0] == 'NOT':
            if op[1].isdigit():
                val[op[3]] = ~int(op[1])
            else:
                val[op[3]] = ~val[op[1]]
        if len(op) == 5:
            if op[0].isdigit():
                val1 = int(op[0])
            else:
                val1 = val[op[0]]
            if op[2].isdigit():
                val2 = int(op[2])
            else:
                val2 = val[op[2]]
        if op[1] == 'AND':
            val[op[4]] = val1 & val2
        if op[1] == 'OR':
            val[op[4]] = val1 | val2
        if op[1] == 'LSHIFT':
            val[op[4]] = val1 << val2
        if op[1] == 'RSHIFT':
            val[op[4]] = val1 >> val2
    except KeyError:
        # print('KeyError, pushing back')
        dq.append(op)
print(val['a'])
tmp = val['a']

# Second phase
val.clear()
val['b'] = tmp
for cmd in lines:
    ops = list()
    ops = cmd.split(' ')
    dq.append(ops)

while dq:
    op = list()
    op = dq.popleft()
    try:
        # print('Trying', op)
        if op[1] == '->':
            if op[2] == 'b':
                continue
            if op[0].isdigit():
                val[op[2]] = int(op[0])
            else:
                val[op[2]] = val[op[0]]
        if op[0] == 'NOT':
            if op[1].isdigit():
                val[op[3]] = ~int(op[1])
            else:
                val[op[3]] = ~val[op[1]]
        if len(op) == 5:
            if op[0].isdigit():
                val1 = int(op[0])
            else:
                val1 = val[op[0]]
            if op[2].isdigit():
                val2 = int(op[2])
            else:
                val2 = val[op[2]]
        if op[1] == 'AND':
            val[op[4]] = val1 & val2
        if op[1] == 'OR':
            val[op[4]] = val1 | val2
        if op[1] == 'LSHIFT':
            val[op[4]] = val1 << val2
        if op[1] == 'RSHIFT':
            val[op[4]] = val1 >> val2
    except KeyError:
        # print('KeyError, pushing back')
        dq.append(op)
print(val['a'])
