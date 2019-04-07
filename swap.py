#!/usr/bin/env python


x = 3
y = 5

def swap(i,o):
    i, o = o,i
    return(i,o)

print(f'x = {x} y = {y}')

#x,y = y,x
x,y = swap(x,y)

print(f'x = {x} y = {y}')