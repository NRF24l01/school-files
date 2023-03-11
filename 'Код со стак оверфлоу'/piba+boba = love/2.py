import random

valera = ""
lena = int(input("Введите длину строки:"))
i = 0
while i <= lena:
    p = random.randint(33, 127)
    valera = valera + chr(p)
    i = i + 1

print(valera)