size = int(input("Введите размер кораблика: "))*2
i = 1
prob = size - 1
while i <= size:
    #res = " " * prob-1 + "*" * i + " " * prob-1
    print(" " * prob-1 + "*" * i + " " * prob-1)
    #print(i)
    #print(prob)
    i = i + 2
    prob = prob - 1