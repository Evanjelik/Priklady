print("Overenie delitelnosti.")

n = input("Zadaj cislo na delenie: ")
while not n:
    n = input("Zadaj cislo na delenie: ")
k = input("Zadaj delitela: ")

while not k:
    k = input("Zadaj delitela: ")


def nula():
    if k ==0:
        print("Delit nulou nejde.")
    else:
        return k

nula()

v = int(n) % int(k)

if v == 0:
    print(n + " je mozne delit " + k)
else:
    print(n + " nie je delitelne " + k)
