import sys

f = sys.argv

if (n := len(f)) == 1:
    print(f'Zadejte prosim vice nez {n} argument')
    sys.exit()
else:
    for pocet in f:
        if pocet.isdigit():
            pocet = int(pocet)
            c = (pocet-32)*5/9
            print(f'{pocet}°Fahrnheita je {c:.2f}° celsia')

