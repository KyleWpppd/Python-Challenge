#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Kyle Wanamaker on 2011-01-13.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import string

def main():
	advanceString(0,0)


def powerUp(x,pow):
	x**=pow
	print x
	
def advanceString(mystring, advance):
	if not mystring or advance:
		mystring = raw_input("Enter mystring: ")
		advance = int(raw_input("Enter shift: "))
		if(advance < 0):
			advance +=26
	outstring = ''
	for mychar in mystring:
		if mychar in string.ascii_letters:
				if ord(mychar)+advance > ord('z'):
					ascii = ord(mychar)-(26-advance)
				else:
					ascii = ord(mychar)+advance
				mychar = chr(ascii)
		outstring+=mychar
	print outstring
			


if __name__ == '__main__':
	main()

