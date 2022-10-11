import sympy
sympy.init_printing(use_latex='mathjax') # Para que se vea bonito


def resolver():
    x= sympy.Symbol('x')
    y= sympy.Function('y')
    
    edo= sympy.Eq(y(x).diff(x),((x**2*y)-y)/(y + 1))
    CI={y(3):1}
    solucion= sympy.dsolve(edo, y(x), ics=CI)
    print(solucion)
    sympy.plot(solucion.rhs, (x, 0, 10), title='Solución de la EDO')
    
 




