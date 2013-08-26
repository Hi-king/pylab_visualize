#!/usr/bin/python
import sys
import math
import random

outputnum=int(sys.argv[1])
lines = [line for line in sys.stdin]

randomizedlinenum=[]
while len(randomizedlinenum)<len(lines) and len(randomizedlinenum)<outputnum:
    randomizedlinenum
    randnum = random.randint(0, len(lines)-1)
    if not randnum in randomizedlinenum:
        randomizedlinenum.append(randnum)
for linenum in randomizedlinenum:
    print lines[linenum],
