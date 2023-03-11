from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import random
import config

# Функция для уменьшения жизни каждую секунду
def check_life():
    ra = random.randint(1,3)
    print(ra)
    if ra == 1:
        # узнаем, какая сейчас жизнь из прогресс бара
        current_life = poop.get()

        # уменьшаем значение на прогрессбаре
        poop.set(current_life - 1)

        # если жизни мало - закрываем приложение
        if current_life <= 1:
            messagebox.showerror(title="Вы проиграли!", message="Зверек умер... :(")
            quit()
        # иначе запускаем функция еще через секунду
        else:
            window.after(1000, check_life)
    elif ra == 2:
        print("45tun98v6v45")

# функция для кормления
def feed():
    # устанавливаем жизнь на максимум
    poop.set(100)

window = Tk()
window.title("ПИТОМЕЦ")

# поскольку жизнь - числовая характеристика, вместо StringVar - IntVar
poop = IntVar()
poop.set(50)
#life = IntVar()
#life.set(50)

# добавляем прогресс-бар
Progressbar(window, variable=poop).pack(padx=50, pady=25)

# добавляем кнопку для увеличения жизни
Button(window, text="Покормить", command=feed).pack(padx=25, pady=25)

# включаем таймер для уменьшения жизни через секунду
window.after(1000, check_life)

mainloop()