#Lets start!

#imports
import data
import time
import winsound  #если виинда
#import simpleaudio  #если макось

#Initeflise


#Funktions:
def start0():
    print("Над вами доктора.")
    time.sleep(0.75)
    print("Они говорят о каком-то П.Е.Р.С.И.К")
    time.sleep(0.75)
    print("О пациэнте О 5")
    time.sleep(0.75)
    print("На часах вы заметили 04.01.211")
    time.sleep(0.75)
    print("Вы снова вырубились...")
    time.sleep(1.75)
    print("Вы очнулись в больничной палате.")
    time.sleep(0.75)
    print("У вас расскалывалась голова, вас подташнивало.")
    time.sleep(0.75)
    print("Вы посмотрели на другие койки там были ужасные трупы.")
    time.sleep(0.75)
    print("Она выглядела заброшеной.")
    time.sleep(0.75)
    print("Вы подняли руку. В ней вы увидели...")
    time.sleep(2)
    print("4 слота. И часы на которых было 04.01.1986")
    time.sleep(0.75)
    print("В первых 2 вы почему-то узнали слоты DDr r128. В 1 из них была какая-то микросхема с пометкой 128TB.")
    time.sleep(0.75)
    print("В 3 слоте, как и в 4 ничего не было.")
    time.sleep(0.75)
    print("Вы мыслено себя поздравили с тем что вы робот. В голове пронеслись слова докторов.")
    time.sleep(0.75)
    print("Вы встали с койки и увидели 3 комнаты.")
    time.sleep(2.75)
    chose1()

def chose1():
    print("Куда пойдём?")
    print("103-Прачечная")
    print("104-Склад")
    print("105-Лабаратория")
    print("0-Да зачем вообще куда-то идти?")
    ans=str(input())
    if(ans=="103"):
        print("w")
    elif (ans == "104"):
        print("a")
    elif (ans == "105"):
        print("w")
    elif (ans == "0"):
        print("Да зачем ты вообше сюда пришёл???????")
        print("Иди думай лучше!")
        time.sleep(167.75)
        chose1()
    else:
        print("Я ничего не понял. Повторите пожалуйста.")
        time.sleep(1)
        chose1()



#Quest start
start0()