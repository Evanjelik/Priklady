print("Budeme pocitat. Zadas dve cisla a ukazem ti vysledok.")
prve_cislo = input("Zadaj prve cislo: ")
while not prve_cislo:
    prve_cislo = input("Zadaj prve cislo: ")
druhe_cislo = input("Zadaj druhe cislo: ")
while not druhe_cislo:
    druhe_cislo = input("Zadaj druhe cislo: ")
vysledok = float(prve_cislo) + float(druhe_cislo)
print("Vysledok je " + str(vysledok))
