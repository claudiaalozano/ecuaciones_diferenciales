import sympy as sym
sym.init_printing(use_latex= True) # Para imprimir en formato LaTeX en la consola 

def resolver():
    y= sym.symbols("f", cls=sym.Function) # Definimos la función f  
    x= sym.symbols("x", real = True) # Definimos la variable x
    
    eq = sym.Eq(y(x).diff(x), x**2*y(x)-y(x)/(1+y(x))) # Definimos la ecuación diferencial
    a = sym.dsolve(eq, ics ={y(3): -1, sym.diff(y(x), x).subs(x, 0): 0}) # Resolvemos la ecuación diferencial
    print("La solución a la ecuación y'= x^2*y-y/(1+y) es:")
    sym.pprint(a) # Imprimimos la solución
resolver()


