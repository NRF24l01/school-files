from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

current_image = None
current_tk_image = None

def open_file():
    global current_image
    global current_tk_image

    path = filedialog.askopenfilename()
    current_image = Image.open(path)
    current_tk_image = ImageTk.PhotoImage(current_image)
    place_for_image.configure(image=current_tk_image)

def rotate():
    global current_image
    global current_tk_image

    if current_image:
        current_image = current_image.transpose(Image.ROTATE_90)
        current_tk_image = ImageTk.PhotoImage(current_image)
        place_for_image.configure(image=current_tk_image)

window = Tk()
window.title("PHOTOSHOP 2077CC ULTRA BE ADOBE THE BEST COMPANY")

place_for_image = Label(window)
place_for_image.pack()

Button(window, text="Открыть файл", command=open_file).pack(pady=20, padx=20)
Button(window, text="Повернуть", command=rotate).pack(pady=20, padx=20)
Button(window, text="Повернуть", command=rotate).pack(pady=20, padx=20)

mainloop()