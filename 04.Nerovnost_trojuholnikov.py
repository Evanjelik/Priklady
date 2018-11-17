print("Po zadani velkosti stran zistime, ci je mozne zostrojit trojuholnik.")
print()

a = input("Zadaj velkost strany a: ")
while not a:
    a = input("Zadaj velkost strany a: ")
b = input("Zadaj velkost strany b: ")
while not b:
    b = input("Zadaj velkost strany b: ")
c = input("Zadaj velkost strany c: ")
while not c:
    c = input("Zadaj velkost strany c: ")


if a + b <= c or a + c <= b or b + c <= a:
    print("Trojuholnik nie je mozne zostrojit.")
else:
    print("Trojuholnik je mozne zostrojit.")