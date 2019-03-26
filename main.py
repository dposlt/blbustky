#!/usr/bin/env python

from sys import argv
from sys import stdout
from time import sleep


#code
if len(argv) != 2:
    exit('Usage: string')

nameOfargv = argv[1]

if nameOfargv.isdigit():
    exit('Please giv me string')

count = 0
while len(nameOfargv) != count:
    for i in nameOfargv:
        stdout.write('{letter} '.format(letter = i))
        stdout.flush()
        sleep(.300)
        count +=1

print('\t')