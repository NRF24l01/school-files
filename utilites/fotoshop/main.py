from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import filters

current_tk_image = ImageTk.PhotoImage(Image.open("main.jpg"))

def open_file():
    global current_tk_image
    path = filedialog.askopenfilename()
    filters.current_image = Image.open(path)
    filters.current_image.show()
    current_tk_image = ImageTk.PhotoImage(image=filters.current_image)
    place_for_image.configure(image=current_tk_image)
    place_for_image.grid(row=3, column=2)
    #filters.current_image.show()

def rotate():
    global current_tk_image
    if filters.current_image:
        filters.current_image = filters.current_image.transpose(Image.ROTATE_90)
        filters.current_image.show()
        current_tk_image = ImageTk.PhotoImage(image=filters.current_image)
        place_for_image.configure(image=current_tk_image)
        place_for_image.grid(row=4, column=3)

def upd():
    place_for_image.configure(image=current_tk_image)
    place_for_image.grid(row=4, column=3)
    print("piba")

window = Tk()
window.title("PyPaint 0.75")

place_for_image = Label(window)
#place_for_image.pack()

Button(window, text="Открыть файл", command=open_file).grid(row=0, column=0)
#Button(window, text="Повернуть", command=rotate).grid(row=1, column=0)
Button(window, text="ЧБшнуть", command=filters.gray).grid(row=1, column=0)
#place_for_image.grid(row=3, column=2)
window.after(1, upd)

mainloop()