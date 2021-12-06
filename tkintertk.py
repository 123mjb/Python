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
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    def getSquareRoot ():  
        x1 = entry1.get()

        label1 = tk.Label(root, text= float(x1)**0.5)
        canvas1.create_window(200, 230, window=label1)
    def multiplication():
        num1, num2 = r.randrange(1, 10), r.randrange(1, 10)
        txt=num1,"X",num2
        ttk.Label(frm2, text=txt).grid(column=0, row=0)
        entry1 = ttk.Entry(frm2) 
        newWindow.create_window(200, 140, window=entry1)
        button1 = ttk.Button(text='Get the Square Root', command=getSquareRoot)
    Label(newWindow,
          multiplication()).pack()
ttk.Label(frm, text="Hello").grid(column=0, row=0)
ttk.Label(frm, text="World!").grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Game", command=openNewWindow).grid(column=1, row=1)          
root.mainloop() # ttk.Button(frm2, text="Game", command=openNewWindow).grid(column=0, row=0, )