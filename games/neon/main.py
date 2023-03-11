from tkinter import *
from PIL import Image, ImageTk
import winsound



window = Tk()

winsound.PlaySound("SONG.wav", winsound.SND_ASYNC)

# открываем картинку luntik.gif, она лежит в одной папке с программой и кладем в переменную luntik_image
# открываем изображение любого формата и кладем его в переменную image_file
im1 = Image.open("1.png")
im2 = Image.open("2.png")
im3 = Image.open("3.png")
im4 = Image.open("4.png")
im5 = Image.open("5.png")
im6 = Image.open("6.png")

# "готовим" изображение к размещению в окне и кладем в переменную vp_image
vi1 = ImageTk.PhotoImage(im1)
vi2 = ImageTk.PhotoImage(im2)
vi3 = ImageTk.PhotoImage(im3)
vi4 = ImageTk.PhotoImage(im4)
vi5 = ImageTk.PhotoImage(im5)
vi6 = ImageTk.PhotoImage(im6)


kliks_or = 0
kliks = StringVar()
im_n=0
pipip=ImageTk.PhotoImage(im1)

def next_im():
    global kliks_or
    global kliks
    global pipip
    global im_n
    kliks_or=kliks_or+1
    kliks.set(kliks_or)
    im_n=im_n+1
    if im_n==1:
        pipip=vi1
    elif im_n==2:
        pipip=vi2
    elif im_n==3:
        pipip=vi3
    elif im_n==4:
        pipip=vi4
    elif im_n==5:
        pipip=vi5
    elif im_n==6:
        pipip=vi6
    else:
        im_n=1
        next_im()
    image_label.configure(image=pipip)



# создаем текстовое поле и указываем, что туда нужно поместить картинку из переменной luntik_image
Label(window, textvariable=kliks, font=("Bernard MT", 25), fg="#FF9966").pack()
#Label(window, image=pipip).pack()
image_label = Label(window, image=pipip)
image_label.pack()
Button(window, text='Плиз! НЕ ЖМИ!!!', height=5, width=10, command=next_im).pack()
mainloop()