import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import random
time = time.time()
window = Tk()
import config


# открываем изображение любого формата и кладем его в переменную image_file
kaka = Image.open("fun.png")
a = ImageTk.PhotoImage(kaka)
# "готовим" изображение к размещению в окне и кладем в переменную vp_image
#kaka_tk = kaka.resize((300, 700), Image.ANTIALIAS)
Label(window, image=a).pack()
#Button(window, text="Покормить", width=30, height=5, command=my_action).pack()

window.title("ТАМАГОЧИ")
def minus():
    global fun
    global poopik
    global food
    ra = random.randint(1,3)
    print(ra)
    if ra==0:
        food=food-1
    elif ra==1:
        poopik=poopik-1
    else:
        fun=fun-1
    print(str(food) + " " + str(poopik) + " " + str(fun))
    window.after(5000, minus)
    if food==0 or poopik==0 or fun==0:
        messagebox.showerror(title="Ваш персонаж погиб!", message="Выш персонаж погиб!")
        exit()
window.after(config.hard, minus)
mainloop()