from tkinter import *
import random
from PIL import Image, ImageTk
import time
window = Tk()

# добавляем статус бар для счета вверху экрана
state_label = StringVar()
Label(window, textvariable=state_label).pack()

c = Canvas(window, width=640, height=640, bg='white')
c.pack()

a = Image.open("as.png")
img1 = ImageTk.PhotoImage(image=a)

# загружаем картинки - астероид, небо и игрок
asteroid_image = img1
player_image = ImageTk.PhotoImage(Image.open("roc.png"))
sky_image = ImageTk.PhotoImage(Image.open("fon.png").resize((640, 640), Image.ANTIALIAS))

# рисуем небо
c.create_image(0, 0, image=sky_image, anchor=NW)

# количество шаров
N = 10

# списки со скоростями
x_speeds = []
y_speeds = []

# список с фигурами
asteroids = []

# создаем N астероидов
for i in range(N):
    # придумываем координаты
    x = random.randint(20, 610)
    y = random.randint(20, 610)

    # создаем астероид - теперь это картинка на базе asteroid_image
    asteroid = c.create_image(x, y, image=asteroid_image, anchor=NW)

    # придумываем скорость
    vx = random.randint(-15, 15)
    vy = random.randint(-15, 15)

    # добавляем астероид в список
    asteroids.append(asteroid)

    # добавляем скорости в списки
    x_speeds.append(vx)
    y_speeds.append(vy)

# создаем игрока на основе картинки
player = c.create_image(300, 300, image=player_image, anchor=NW)

# переменная для хранения жизни
life = 3

# длительности игры
game_time = 0

# выводим стартовое время вверху экрана
state_label.set("Время в игре: " + str(game_time))

def move_ball():
    global game_time
    global life
    # TODO: получить левую верхнюю коодинату игрока
    player_x1, player_y1 = c.coords(player)

    # TODO: вычислить правую нижнюю координату игрока
    player_x2, player_y2 = player_x1 + 30, player_y1 + 30
    # для каждого астероида из N
    for i in range(N):
        # берем номер астероида c номером i из списка
        asteroid = asteroids[i]

        # и его скорости
        vx = x_speeds[i]
        vy = y_speeds[i]

        # получаем текущие координаты астероида
        # поскольку у картинки в отличие от овала только две координаты (левого верхнего угла),
        # мы сами вычисляем правую нижнюю координату
        x1, y1 = c.coords(asteroid)
        x2 = x1 + 40
        y2 = y1 + 40

        # TODO: если астероид пересекается с игроком - уменьшить жизнь
        if (player_x1<x1<player_x2 or  player_x1<x2<player_x2) and (player_y1<y1<player_y2 or player_y1<y2<player_y2):

            life = life - 1
        # TODO: если жизнь на нуле - закрыть игру tk.destroy()
        if life <= 0:
            window.destroy()

        # если астероид на границе по x - развернуть скорость по x
        if x1 <= 0 or x2 >= 640:
            vx *= -1
        # аналогично по y
        if y1 <= 0 or y2 >= 640:
            vy *= -1

        # сохраняем скорости обратно в список
        x_speeds[i] = vx
        y_speeds[i] = vy
        print(asteroid, vx, vy)
        # передвигаем астероид
        c.move(asteroid, vx, vy)

    # повторяем через полсекунды
    c.after(50, move_ball)

    # TODO: увеличиваем время жизни на 0.05
    game_time = game_time + 0.05
    # TODO: обновляем поле вверху экрана
    state_label.set("Время в игре: "+str(int(game_time))+"  Жизней: "+str(life))

# спустя полсекунды (50 мс) после запуска выполнить moveBal

def move_player(event):
    c.coords(player,event.x,event.y)

# при нажатии любой клавишы вызываем keyDown
window.bind('<Motion>', move_player)

c.after(5000, move_ball)

mainloop()