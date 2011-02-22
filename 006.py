#!/usr/bin/env python
# encoding: utf-8
"""
006.py

Created by Kyle Wanamaker on 2011-01-14.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import re
import string
import zipfile



def main():
    #readzip()
    readfile()
    #collectcomments()
    pass


def readzip():
    zf = zipfile.ZipFile("/Users/kwan77/Downloads/channel.zip", 'r')
    print zf, zf.infolist()
    print "====================================="
    print zf.namelist()
    for obj in zf.infolist():
        sys.stdout.write( obj.comment)
    
    
def h1(s):
    preg = re.compile('(?<=nothing is )[0-9]{1,5}')
    result = preg.search(s)
    if result:
        return (True, result.group(0))
    else:
        return (False,)

def readfile():
    loc = "90052"
    fileorder = (loc,)
    collectcomments(loc)
    while (True):
        f = open("/Users/kwan77/Downloads/channel/%s.txt" % loc, 'r')
        if f:
            for line in f:
                res = h1(line)
                if res[0]:
                    #sys.stdout.write(loc+"--->"+res[1]+'\n')
                    loc = res[1]
                    f.close()
                    collectcomments(loc)
                    break
                else:
                    print ("###ERROR###", line)
                    f.close()
                    return
        else:
            print "error opening file"
    return
    

def collectcomments(fnum):
    ext = ".txt"
    loc = str(fnum)+ext
    filename = "/Users/kwan77/Downloads/channel.zip"
    if ( zipfile.is_zipfile(filename) ):
        zf = zipfile.ZipFile(filename, 'r')
        if zf:
            data = zf.getinfo(loc)
            sys.stdout.write(data.comment)
            zf.close()
                
            


if __name__ == '__main__':
    main()

