#!/us/bin/env python
#coding: utf-8
import os
import sys

def count(file):
	count = 0
	for line in file:
		if 55000 >= int(line):
			if int(line) >= 65535:
				count +=1
	print (count)
	
if __name__ == '__main__':
	file = input("日志文件名：")
	count("./"+file)