#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Kyle Wanamaker on 2011-01-14.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import urllib
import re
import time


def main():
	initializeSomeShit()

def initializeSomeShit():
	loc = "72758"
	loc = doSomeShit2(loc)
	return

	

def doSomeShit(loc):
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
#	page = urllib.urlopen(url+str(loc))
	s = urllib.urlopen(url+str(loc)).read()
#	s = page.read()
	sys.stdout.write(url + "   -> ")
#	page.close()
	preg = re.compile('(?<=the next nothing is )[0-9]{3,5}')
	result = preg.search(s)
	if result:
		loc = result.group(0)
		print loc
		doSomeShit(loc)
	else:
		print s


def doSomeShit2(loc):
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
	preg = re.compile('(?<=the next nothing is )[0-9]{3,5}')
	while True:
		s = urllib.urlopen(url+str(loc)).read()
		sys.stdout.write(url + "   -> ")
		result = preg.search(s)
		if result:
			loc = result.group(0)
			print loc
		else:
			print("\n### ERROR ###  see: "+url+loc)
			break

	

if __name__ == '__main__':
	main()

