monney = int(input("Введите доход за месяц: "))
bomjes = int(input("Введите количество сотрудников: "))

trates = 0
i = 1
while i <= bomjes:
    tr = int(input("Введите трату на сотрудника "+ str(i)  + ":"))
    trates = trates + tr
    i = i + 1

if monney > trates:
    do = monney - trates
    print("У вас осталось: "+str(do)+" руб.")
elif monney == trates:
    print("Надо работать лучше. Тогда у вас не будет оставатся 0 рублей.")
elif monney < trates:
    print("Вы поработали в убыток.")
    di = trates - monney
    print("Вам нужно взять кредт в банке на: "+str(di)+" руб.")