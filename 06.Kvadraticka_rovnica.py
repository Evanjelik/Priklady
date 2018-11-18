import math

print('Vypocitam ti kvadraticku rovnicu.\nZadaj koeficienty a,b,c do tvaru kvadratickej rovnice ax^2 + bx + c = 0\n')

a = input('Zadaj koeficient a: ')

while not a != 0:
    print('a nesmie byt nula')
    a = input('Zadaj koeficient a: ')

b = input('Zadaj koeficient b: ')
c = input('Zadaj koeficient c: ')

d = int(b)**2 - 4*int(a)*int(c)


if d > 0:
    x1 = (-int(b) + math.sqrt(d))/(2*int(a))
    x2 = (-int(b) - math.sqrt(d))/(2*int(a))
    print('Korene\n''x1 = ' + str(x1) + '\nx2 = ' + str(x2))
elif d == 0:
    x = (-int(b) / (2 * int(a))
    print('Je len jedno riesenie a to: x = ' + str(x))
else:
    print('Kvadraticka rovnica nema riesenie')
