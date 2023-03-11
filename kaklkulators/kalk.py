import tkinter
import tkinter.messagebox
count1=""
count2=""

def one():
    global count1
    count1 = count1+"1"
    print(count1)

window = tkinter.Tk()
window.title("ОЧЕНЬ КРУТОЙ КАЛЬКУЛЯТОР!")

data1 = tkinter.StringVar()
data2 = tkinter.StringVar()

tkinter.Entry(window, width=50, font=("Fixedsys"), textvariable=data1).pack()
tkinter.Label(window, width=20, fg="#BC5D58", textvariable=data1, font=("Fixedsys", 10)).pack()
tkinter.Entry(window, width=50, font=("Fixedsys"), textvariable=data2).pack()
tkinter.Label(window, width=20, fg="#BC5D58", textvariable=data2, font=("Fixedsys", 10)).pack()
tkinter.Button(window, text="1", width=30, height=30, command=one).pack()


tkinter.mainloop()