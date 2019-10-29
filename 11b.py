#!/usr/bin/python3


def incr(passwd):
    i = 7
    remainder = 1
    while i > 0:
        if remainder:
            if ord(passwd[i]) == ord('z'):
                passwd[i] = 'a'
            else:
                passwd[i] = chr(ord(passwd[i])+1)
                remainder = 0
        i -= 1


def chkpass(tstpass):
    stage2pass = True
    for x in tstpass:
        if x in ('i', 'o', 'l'):
            stage2pass = False
    if stage2pass is False:
        # print('Stage2 failure')
        return False
    num = [ord(x) for x in tstpass]
    prev = 0
    stage1pass = False
    count = 0
    for x in num:
        if (x-prev) == 1:
            count += 1
        else:
            count = 0
        if count == 2:
            stage1pass = True
        prev = x
    if stage1pass is False:
        # print('Stage1 failure')
        return False
    stage3pass = False
    prev = ''
    pairs = set()
    for x in tstpass:
        if x == prev:
            pairs.add(x)
        prev = x
    if len(pairs) > 1:
        stage3pass = True
    return stage3pass


def find_next_passwd(cpasswd):
    lpass = list(cpasswd)
    incr(lpass)
    # print(lpass)
    while not chkpass(lpass):
        incr(lpass)
        # print(lpass)
    newpasswd = ''.join(lpass)
    return newpasswd


with open('11.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
curpass = lines[0]
newpass = find_next_passwd(curpass)
newpass = find_next_passwd(newpass)
print(newpass)
