import data
import chooses
import time
import end

def loundry():
    data.loundry1=1
    print("Вы вошли в прачечную.")
    time.sleep(1)
    print("Тут ржавые стиралки.")
    time.sleep(0.75)
    print("Вы увидели карту по виду похожую на вашу карту питания из школы")
    print("Возьмём?")
    time.sleep(1)
    print("1-Да")
    print("2-Нет")
    print("3-Обрадоватся, покричать и взять")
    ans=str(input())
    if(ans=="1"):
        print("Вы взяли карту")
        data.backpack["card"]="ok"
    elif(ans=="2"):
        print("Вы не взяли карту")
        data.backpack["card"] = "none"
    elif(ans=="3"):
        end.alternative_end()
    else:
        print("Я вас не понял. Попробуйте ещё раз.")
        loundry()
    chooses.chose2()

def labaratory():
    data.labaratory1=1
    print("Вы вошли в лабораторию.")
    print("На удивление она не так заброшена.")
    print("Вы увидели какую-то микросхему:")
    print(data.memory)
    print("Попробовали вставить:")
    print("Она подошла в 3 слот!!!")
    print("Вы ощютили такой прилив знаний...")
    data.backpack["memory"]="ok"
    print("Вы очнулись через 2 часа.")
    print("Всё это время вы изучали информацию которая была в этом модуле.")
    print("Вы почему то выделили: " + str(data.final_password) + " " + str(data.password))
    print("Вы продолжили изучать эту лаюораторию")
    chooses.chose3()

def storage():
    data.storaje=1
    print("Вы вошли на старый полуразрушеный склад")
    print("Вы увидели микросхему. Она подошла во 2 слот.")
    print(data.ram)
    print("У вас в голове промелькнуло:")
    print("256ТБ ОЗУ")
    data.backpack["ram"]="ok"
    chooses.chose4()