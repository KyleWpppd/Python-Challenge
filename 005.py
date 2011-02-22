#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Kyle Wanamaker on 2011-01-14.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import pickle


def main(): 
	unpickleSomeShit()
	return


def unpickleSomeShit():
	f = open("banner.p", 'rb')
	unp = pickle.load(f)	
	print unp
	for loc,line in enumerate(unp):
		#print loc,line
		sys.stdout.write(str(loc) + " ")
		out = [ch * count for ch, count in line]
		print"".join(out)
		"""
		for tup,qty in line:
				
				sys.stdout.write(tup)
				qty -= 1
		sys.stdout.write('\n')
		"""

if __name__ == '__main__':
	main()

