#!/usr/bin/python
import sys
import math
items = [float(item.rstrip()) for item in sys.stdin]
maxitem = max(items)
for item in items:
    print math.floor(item*10/maxitem)/10.0
