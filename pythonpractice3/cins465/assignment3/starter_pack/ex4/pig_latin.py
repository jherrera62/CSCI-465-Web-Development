#!/usr/bin/env python
import sys
list=[]
con=""
str=""
for line in sys.stdin:
	if line[0] in ['A','E','I','O','U']:
		str+=line.strip()+"-yay"
		str+="\n"
	else:
		list.append("-")
		for i in range(len(line)):
			list.append(line[i].lower())
			if line[i+1] in ['a','e','i','o','u']:
				list.append("ay")
				con=line.split()+list
				for line in con:
					str+=line
				str+="\n"
				list.clear()
				break
str=str.lower()
str=str.split()
for line in str:
	if line[0] not in ['a','e','i','o','u']:
		for i in range(len(line)):
			if line[i+1] in ['a','e','i','o','u']:
				print(line[i+1:])
				break
	else:
		print(line)
