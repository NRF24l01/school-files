from tkinter import *
# импортируем функционал для работы с картинками из pillow, которую мы только что установили
from PIL import Image, ImageTk

win = Tk()

current_image = Image.open("main.jpg")
#current_tk_image = ImageTk.PhotoImage(current_image)

def gray():
    global current_image
    # цикл по всем пикселям
    # img.width - ширина картинки
    # img.height - высота картинки
    for i in range(current_image.width):
        for j in range(current_image.height):
            # получаем цвет
            r, g, b = current_image.getpixel((i, j))

            in1 = r + g + b
            # in12 = in1 / 3.0
            # print(type(in1))
            in12 = int(in1 / 3)

            r = in12
            g = in12
            b = in12

            # сохраняем пиксель обратно
            current_image.putpixel((i, j), (r, g, b))

    # показываем результат
    current_image.show()

#def two_kolor():