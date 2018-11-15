print("Overenie delitelnosti.")

n = input("Zadaj cislo na delenie: ")
k = input("Zadaj delitela: ")

v = int(n) / int(k)


# nie je to az taky zly napad, no da sa to ovela jednoduchsie
if isinstance(v, int):
    print(n + " je mozne delit " + k)
else:
    print(n + " nie je delitelne " + k)


# skus si pozriet, co by ti vratilo 5 % 2
# link : https://realpython.com/python-operators-expressions/ v casti Arithmetic Operators > Modulo 
# podobne priklady sa riesia cez to, kedze to dava jednoznacnejsi zmysel

# poznamky k rieseniu :
# - co sa stane, ak za premennu k dam nulu ? 
# - co sa stane, ak mu odenterujem prazdny vstup ?
