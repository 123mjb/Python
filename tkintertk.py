import random as r
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
def openNewWindow():
    newWindow = Toplevel(root)
    frm2=ttk.Frame(newWindow, padding=10)
    frm2.grid()
    enter = ttk.Entry(frm2)
    newWindow.title("New Window")
    newWindow.geometry("150x100")
    def multiplication():
        num1, num2 = r.randrange(1, 10), r.randrange(1, 10)
        txt=num1,"X",num2
        ttk.Label(frm2, text=txt).grid(column=0, row=0)
        enter.grid(column=0, row=1)
        def getinp():
            i = enter.get()
            if i == num1 * num2:
                ttk.Label(frm2, text="Right!").grid(column=0, row=4)
                multiplication()
            else:
                ttk.Label(frm2, text="Wrong").grid(column=0, row=4)
        btn = ttk.Button(frm2, text='Enter', command=getinp())
        btn.grid(column=0, row=3)
    Label(newWindow,
          multiplication()).pack()
ttk.Label(frm, text="Hello").grid(column=0, row=0)
ttk.Label(frm, text="World!").grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Game", command=openNewWindow).grid(column=1, row=1)          
root.mainloop() # ttk.Button(frm2, text="Game", command=openNewWindow).grid(column=0, row=0, )