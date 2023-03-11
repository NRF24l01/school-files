import random
valera = ""
lena = int(input("Высота: "))
i1 = 0
i = 1
while i1 <= lena:
    while i <= i1:
        p = random.randint(0, 256)
        valera = valera + chr(p)
        i = i + 1
    print(valera)
    i = 1
    valera = ""
    i1 = i1 + 1