from PIL import Image, ImageTk
import time

hard=2500   #Скорость умирания в милисикундах

funi = ImageTk.PhotoImage(Image.open("fun.png"))
gamei = ImageTk.PhotoImage(Image.open("game.png"))
hungryi = ImageTk.PhotoImage(Image.open("hungry.png"))
nfuni = ImageTk.PhotoImage(Image.open("nfun.png"))
poopi = ImageTk.PhotoImage(Image.open("poop.png"))

#feed
lfet = 0    #Время последнего кормления
feed = 100   #Уровень кормления
mfe = 100    #Макс корм
sffe = 10    #Секунду на еденицу

#poop
lpot = 0    #Время последний чистки
poop = 100   #Уровень грязи
mpo = 100    #Макс грязь
sfpo = 10    #Секунду на еденицу

#fun
lfut = 0    #Время последней игры
fun = 100    #Уровень веселья
mfo = 100    #Макс веселье
sffu = 10    #Секунду на еденицу

def WhFe():
    # сколько времени прошло с прошлого кормления
    elti = time.time() - lfet

    # жизнь не может быть меньше нуля
    fea = int(max(0, int(mfe - elti / sffe)))
    return fea

def WhPo():
    # сколько времени прошло с прошлого кормления
    elti = time.time() - lpot

    # жизнь не может быть меньше нуля
    poa = int(max(0, int(mpo - elti / sfpo)))
    return poa

def WhFu():
    # сколько времени прошло с прошлого кормления
    elti = time.time() - lfut

    # жизнь не может быть меньше нуля
    fea = max(0, int(mfe - elti / sffe))
    return(fea)