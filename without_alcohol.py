#!/usr/bin/env python

def days():
    with open('days_without_alcohol.txt','r+') as dwa:
        is_date = dwa.readline()
        if len(is_date) > 0:
            is_date = int(is_date) + 1
            
            dwa.write(str(is_date))
        else:
            dwa.write('1')



days()



