import time
import locatios
import data
import end

def chose1():
    print("Куда пойдём?")
    print("103-Прачечная")
    print("104-Склад")
    print("105-Лабаратория")
    ans=str(input())
    if(ans=="103"):
        if data.loundry1==0:
            locatios.loundry()
        else:
            chose2()
    elif (ans == "104"):
            if data.storaje == 0:
                locatios.storage()
            else:
                chose3()
    elif (ans == "105"):
            if data.labaratory1 == 0:
                locatios.labaratory()
            else:
                chose4()
    else:
        print("Я ничего не понял. Повторите пожалуйста.")
        time.sleep(1)
        chose1()

def chose2():
    print("Вы увидели окно. Что сделаем?")
    time.sleep(1)
    print("1-Вылезем")
    print("2-Пойдём обратно")
    ans=input()
    if (ans=="1"):
        print("Вы упали в овраг и ржавый прут проткнул вас насквозь.")
        time.sleep(1)
        print("Вы погибли от столбняка и кровоизлияния")
        exit()
    elif (ans=="2"):
        chose1()
    else:
        print("Я вас непонял. Попробуйте пожалуйста другой вариант")
        chose2()

def chose3():
    print("Вы увидели подвестной мост на гиганской дырой.")
    print("Пойдём?")
    print("1-Да")
    print("2-Вернёмся обратно")
    ans=input()
    if (ans=="1"):
        if (data.backpack["geyger"]=="ok"):
            print("Вы вставили дозиметр в какую-то ложу и мост превратился в портал.")
            print("Вы в него вошли.")
            print("ПОБЕДА!!!")
            print("В игре 3 концовки. Возможно вы прошли не все")
        else:
            print("Мост оказался очень хлипким, и ты упал в лаву((((")
            exit()
    elif (ans=="2"):
        print("Вы пошли обратно")
        chose1()

def chose4():
    print("Куда пойдём?")
    print("1-Вперёд")
    print("2-Назад")
    if (data.dos==0):
        print("3-Вниз")
    ans=input()
    if (ans=="1"):
        chouse5()
    elif (ans=="2"):
        chose1()
    elif (ans=="3" and data.dos==0):
        print("Вы спустились вниз и увидели дозиметр")
        print("Вы его взяли и поднялись на верх")
        data.backpack["geyger"]="ok"
        data.dos=1
        chose4()

def chouse5():
    if data.backpack["ram"]=="ok" and data.backpack["memory"]=="ok":
        end.best_end()
    else:
        print("Вам чего-то нехватает.")
        print("Побробуйте походить по другим комнатам.")
        chose1()
