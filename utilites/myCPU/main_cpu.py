import psutil
from tkinter import *
from PIL import Image, ImageTk

#print("CPU load:", psutil.cpu_percent(), '%')
#print("Memory load:", psutil.virtual_memory().percent, '%')
#print("Disk usage:", psutil.disk_usage("/").used // 1000000000, 'GB /', psutil.disk_usage("/").total // 1000000000, 'GB')

window = Tk()
window.title("THE BEST PROGRAM FOR YOUR CPU!")

cput = StringVar()
hddt = StringVar()
ramt = StringVar()

def upd():
    global cput
    global hddt
    global ramt
    cput.set(str(psutil.cpu_percent()))
    ramt.set(str(psutil.virtual_memory().percent))
    #print(type(psutil.cpu_percent()))
    #print(type(psutil.virtual_memory().percent))
    #print(type(psutil.disk_usage("/").used // 1000000000))
    window.after(1000, upd)

Label(window, textvariable=cput, font=("Bernard MT", 25), fg="#FF9966").grid(column=0, row=0)
Label(window, textvariable=ramt, font=("Bernard MT", 25), fg="#FF9966").grid(column=0, row=1)
Label(window, textvariable=hddt, font=("Bernard MT", 25), fg="#FF9966").grid(column=0, row=2)

window.after(1000, upd)

mainloop()