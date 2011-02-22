#!/usr/bin/env python
# encoding: utf-8
"""
003.py

Created by Kyle Wanamaker on 2011-01-14.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import re


def main():
	regexmatch()

def regexmatch():
	f = open("003.txt")
	preg = re.compile('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]')
	for line in f:
		result = preg.search(line)
		if result:
			print result.group(0)
	f.close()
		
	

if __name__ == '__main__':
	main()

