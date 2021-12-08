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
    Label(newWindow,ttk.Button(frm2, text="Load", command=multiplication()).grid(column=0, row=0)).pack()
def crash():
    while True:
        openNewWindow()
ttk.Label(frm, text="Hello").grid(column=0, row=0)
ttk.Label(frm, text="World!").grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Broken Game", command=crash).grid(column=1, row=1)          
root.mainloop() # ttk.Button(frm2, text="Game", command=openNewWindow).grid(column=0, row=0, )