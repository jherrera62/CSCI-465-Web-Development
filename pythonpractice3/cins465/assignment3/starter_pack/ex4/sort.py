#!/usr/bin/env python
import sys
list=[]
for line in sys.stdin:
	list.append(line)
list.sort()
for line in list:
	print(line,end="")
