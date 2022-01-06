import random as r
from tkinter import *
from tkinter import ttk
import newwindow as nw
root = Tk()
frm = ttk.Frame(root, padding=10)
btn = ttk.Button(frm, text="New Window", command=nw.open(root)).grid(column=0, row=0)
frm.grid()

root.mainloop()