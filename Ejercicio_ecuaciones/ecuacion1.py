import sympy as sym
sym.init_printing(use_latex= True) # Para imprimir en formato LaTeX en la consola 

def resolver_1():
    y= sym.symbols("f", cls=sym.Function) # Definimos la función f  
    x= sym.symbols("x", real = True) # Definimos la variable x
    
    eq = sym.Eq(y(x).diff(x), (x**2*y(x)-y(x))/(y(x)+1)) # Definimos la ecuación diferencial
    a = sym.dsolve(eq, ics={y(3): -1}) # Resolvemos la ecuación con la condición inicial
    print("La solución a la ecuación y'= (x^2*y-y)/(y+1) es:")
    sym.pprint(a) # Imprimimos la solución

resolver_1()