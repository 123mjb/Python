import tkinter as tk
from sympy import solve
from sympy.abc import x, y, z, a, b
from sympy.parsing.sympy_parser import parse_expr

def solve_meThis(string_):
    try:
        lhs =  parse_expr(string_.split("=")[0])
        rhs =  parse_expr(string_.split("=")[1])
        solution = solve(lhs-rhs)
        return solution
    except:
        print("invalid equation")
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()
entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)
def solve():  
    x1 = entry1.get()
    label1 = tk.Label(root, text= solve_meThis(x1))
    canvas1.create_window(200, 230, window=label1)  
button1 = tk.Button(text='Solve Equation', command=solve)
canvas1.create_window(200, 180, window=button1)
root.mainloop()