import sys

f = sys.argv

if (n := len(f)) < 2: #  arguments == programme name (temp.py)
    print(f'Use more then {n} arguments')
    sys.exit()
elif len(f) > 3:
    print('Too much arguments')
    sys.exit()

if f[2] == 'f' or f[2] == 'F':     #from fahrnheit to celsia
    if (pocet := f[1]).isdigit():
        c = (int(pocet)-32)*5/9
        print(f'{pocet}° Fahrnheint is {c:.2f}° celsia')

elif f[2] == 'c' or f[2] == 'C':   #from celsia to fahrnheit
    if (pocet := f[1]).isdigit():
        c = (9*int(pocet))/5 + 32
        print(f'{pocet}° celsia  je {c:.2f}° Fahrnheint')

elif f[2] != 'f' or f[2] != 'c':
    print('Wrong argument. You can use "f" or "c" only')