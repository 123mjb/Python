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

valid_text = "1/4*x+ 1 = 1/6*x+ 1/2"
print(solve_meThis(valid_text))