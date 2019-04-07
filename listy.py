#!/usr/bin/env python

from cs50 import get_int


numbers = []

while True:

    number = get_int("Number: ")

    if not number:
        break

    if not number.isdigit():
        print('variable is not digit')
        break

    numbers.append(number)

for number in numbers:
    print(number,end=" ")


