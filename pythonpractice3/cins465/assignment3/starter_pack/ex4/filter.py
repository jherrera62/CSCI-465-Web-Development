#!/usr/bin/env python
import sys
for line in sys.stdin:
	cline=line.split(',')
	cline=line.split()
for line in cline:
	bline=line.replace(",","")
	print(bline)
