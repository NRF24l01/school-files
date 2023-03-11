import random
print("Когда оплата нашей работы, РОСТИСЛАВ?????????")
valera = ""
lena = int(input("Высота: "))
nasta = int(input("Ширина: "))
i1 = 1
i = 1
while i1 <= lena:
    while i <= nasta:
        p = random.randint(0, 256)
        valera = valera + chr(p)
        i = i + 1
    print(valera)
    i = 1
    valera = ""
    i1 = i1 + 1

