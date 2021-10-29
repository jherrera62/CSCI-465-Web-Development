#!/usr/bin/env python
import sys
listt=[]
for line in sys.stdin:
	listt.append(line)
listt=list(set(listt))
listt.sort()
for line in listt:
	print(line,end="")
