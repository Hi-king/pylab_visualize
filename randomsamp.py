#!/usr/bin/python
import sys
import math
import random

lines = [line for line in sys.stdin]
if(len(sys.argv)>1):
    outputnum=int(sys.argv[1])
else:
    outputnum=len(lines)

randomizedlinenum=[]
for i in xrange(outputnum):
    randi = random.randint(i, len(lines)-1)
    lines[i], lines[randi] = lines[randi], lines[i]
for i in xrange(outputnum):
    print lines[i],


# while len(randomizedlinenum)<len(lines) and len(randomizedlinenum)<outputnum:
#     randomizedlinenum
#     randnum = random.randint(0, len(lines)-1)
#     if not randnum in randomizedlinenum:
#         randomizedlinenum.append(randnum)
# for linenum in randomizedlinenum:
#     print lines[linenum],
