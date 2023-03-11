import tkinter
import tkinter.messagebox

def but():
    tkinter.messagebox.showerror(message=label_var.get())

window = tkinter.Tk()
window.title("PELMENI IS GOOD")
label_var = tkinter.StringVar()
label_var.set("Ghbdtnuergueguhrh")

tkinter.Label(window, width=100, fg="#0000BB", textvariable=label_var, height=50, font=("Calibri", 50)).pack()
but()

tkinter.Entry(window, width=10,)

tkinter.mainloop()