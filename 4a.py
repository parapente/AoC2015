#!/usr/bin/python3
import hashlib
import re

with open('4.dat') as f:
    data = f.read()
i = 1
while not re.match("00000", hashlib.md5((data+str(i)).encode('utf-8')).hexdigest()):
    i += 1
print(i)
