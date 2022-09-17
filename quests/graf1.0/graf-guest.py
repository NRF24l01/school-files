#Okay! lets start
import time
import picture
import winsound

winsound.PlaySound('musik', winsound.SND_ASYNC)

#kart4, helts_kit, key
Backpuck = ['none', 'none', 'none']

def totem_liftf5():
    print("Используем тотем?")
    print("1-Да")
    print("2-Нет")
    ans = str(input())
    if (ans == "2"):
        print("Вы погибли")
        start0()
        exit()
    elif (ans == "1"):
        print("Вы какой-то магией востановились!")
        Backpuck[1] = "none"
        time.sleep(1)
        print("Что делаем дальше?")

def lift4():
    print("Дверь открылась.")
    time.sleep(1.5)
    print("Это был лифт")
    time.sleep(1)
    print("Внутри вы увидели ключ и тотем бесмертия.")
    print("Вы это взяли и нажали на кнопку в лифте")
    Backpuck[1]="ok"
    Backpuck[2]="ok"
    time.sleep(2.5)
    print("Лифт двинулся, а потом резко упал.")
    time.sleep(3)
    print("Вы очень сильно травмированы.")
    time.sleep(1.75)
    totem_liftf5()
    print("Используем тотем?")
    print("1-Да")
    print("2-Нет")
    ans=str(input())
    if(ans=="2"):
        print("Вы погибли")
        start0()
        exit()
    elif(ans=="1"):
        print("Вы какой-то магией востановились!")
        Backpuck[1]="none"
        time.sleep(1)
        print("Что делаем дальше?")
        print("1-Танцуем уги буги")
        print("2-С помощью ключа вырезаем крышу???")
        print("3-Чилим")
        answ=str(input())
        if(answ=="1"):
            time.sleep(1)
            print("Вы начали танцевать и лифт развалился окончательно. Вас завалило")
            print("Вы погибли")
            start0()
        elif(answ=="2"):
            time.sleep(1)
            print("Вы начали вырезать крышу но вашу руку порезал кусок ржавой крыши.")
            Backpuck[2]="none"
            print("Вы погибли от столбняка")
            start0()
        elif(answ=="3"):
            time.sleep(1)
            print("Вы подождали 1 час...")
            time.sleep(1)
            print("Вас спасли!")
            print(picture.helper)
            print("ПОБЕДА!!!!")
        else:
            print("Непонял. Попробуй ещё.")
            lift4()
    else:
        print("Непонял. Попробуй ещё.")
        lift4()

def non3():
    print("Вы остались тут")
    print("Через 10 минут вы увидели Его")
    if(Backpuck[0]=='none'):
        print("Вы погибли")
        start0()
        exit()
    else:
        time.sleep(1)
        print("Вы погибли")
        print(picture.duy)
        print("У вас была карта которую поднял Он.")
        time.sleep(2)
        print("Он вышел за пределы Своего здания.")
        time.sleep(3)
        print("Мир уничтожен")
        exit()

def out3():
    print("Вы вышли из комнаты и видете лифт.")
    print("К нему нужен ключ доступа")
    print("Что сделаем?")
    if(Backpuck[0]=="ok"):
        print("Вы приложили ключ")
    else:
        print("Вы порезали провода в системе идентификации")
        print(picture.plug)
    lift4()


def exit_YN3():
    print("Выйдем?")
    print("1-Да")
    print("2-Нет")
    answer = str(input())
    if (answer == "1"):
        out3()
        # print("Вы выбрали 1")
    elif (answer == "2"):
        non3()
        # print("Вы выбрали 2")
    else:
        print("Попробуёте ещё.")
        exit_YN3()


def take_card2():
    Backpuck[0]='ok'
    print("Вы подобрали карту")
    print("Вы увидели дверь.")
    exit_YN3()


def non2():
    Backpuck[0]='none'
    print("Вы не взяли карту")
    print("Вы увидели дверь.")
    exit_YN3()

def noise2():
    print("Вы начали кричать и привлекли Его внимание")
    print("Вы погибли")
    print(picture.duy)
    start0()
    exit()


def answer2():
    print("1-Взять")
    print("2-Оставить")
    print("3-Покричать от радости и взять")
    answer = str(input())
    if (answer == "1"):
        take_card2()
        # print("Вы выбрали 1")
    elif (answer == "2"):
        non2()
        # print("Вы выбрали 2")
    elif (answer == "3"):
        noise2()
        # print("Вы выбрали 3")
    else:
        print("Попробуёте ещё.")
        answer2()


def up1():
    print("Вы встали.")
    print("Увидели карту доступа 4 уровня")
    time.sleep(1)
    answer2()


def non1():
    print("Вы продолжили лежать")
    time.sleep(1)
    print("Пролежади час...")
    time.sleep(1)
    print("Пролежали два...")
    time.sleep(3)
    print("Пролежали шесть...")
    time.sleep(5)
    print("Пролежали сутки...")
    time.sleep(3)
    print("Моргнули...")
    time.sleep(1)
    print("Увидели Его")
    time.sleep(1)
    print("Вы погибли")
    print(picture.duy)
    start0()
    exit()

def sleeep1():
    print("Вы легли спать и проснулись по ощущениям через 12 дней.")
    print("Открыли глаза иии")
    time.sleep(1)
    print("Увидели Его...")
    time.sleep(1)
    print("Вы погибли")
    print(picture.duy)
    start0()
    exit()



def answer1():
    print("Что сделаем?")
    print("1-Встать")
    print("2-Остатся лежать")
    print("3-Уснуть")
    answer = str(input())
    if (answer == "1"):
        up1()
        #print("Вы выбрали 1")
    elif (answer == "2"):
        non1()
        #print("Вы выбрали 2")
    elif (answer == "3"):
        sleeep1()
        #print("Вы выбрали 3")
    else:
        print("Попробуёте ещё.")
        answer1()

def start0():
    print("Итак. Нажмите что нибудь на клавиатуре чтоб осмотрется")
    input()
    print("Хммм")
    print('''<Осматриваетесь>''')
    time.sleep(0.5)
    print('''<Осматриваетесь>''')
    time.sleep(0.5)
    print('''<Осматриваетесь>''')
    time.sleep(0.5)
    print("Вы растроились")
    time.sleep(1)
    print("Во время осмотра вы увидели на себе костюм")
    time.sleep(0.1)
    print("С номером")
    time.sleep(1)
    print("666")
    time.sleep(2)
    print("Когда вы подняли голову вы увидели ужасную")
    time.sleep(0.1)
    print("Больницу")
    time.sleep(0.2)
    print("Это не просто больница...")
    time.sleep(1)
    print("Это разушеная кем-то(или чем-то) палата в которой ржавые кровати и ржавые прутья торчашие из стен")
    answer1()

start0()