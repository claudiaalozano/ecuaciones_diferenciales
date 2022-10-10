from sympy import *
from sympy.interactive import printing

printing.init_printing(use_latex= True)

def lin():
    print("\n")

    x = symbols("x")
    y = symbols("y")
    z = symbols("z")
    

    display(x)
    display(y)

    f = Function("f")("x")
    g = Function("g")("y")
