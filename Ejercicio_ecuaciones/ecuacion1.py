import sympy as sym
sym.init_printing(use_latex= True) # Para imprimir en formato LaTeX en la consola 
y= sym.symbols("f", cls=sym.Function) # Definimos la función f  
x= sym.symbols("x", real = True) # Definimos la variable x
