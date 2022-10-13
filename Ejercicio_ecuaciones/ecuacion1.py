import sympy
<<<<<<< HEAD
sympy.init_printing(use_latex='mathjax') # Para que se vea bonito

# ecuacion diferencial
# y' = 2xy


def resolver():
    x= sympy.Symbol('x')
    y= sympy.Function('y')
    
    edo= sympy.Eq(y(x).diff(x), 2*x*y(x))
    CI={y(3):1}
    solucion= sympy.dsolve(edo, y(x), ics=CI)
    print(solucion)
    sympy.plot(solucion.rhs, (x, 0, 10), title='Solución de la EDO')
    
if __name__ == '__main__':
    resolver()

=======
>>>>>>> bd565c3761f147e628b70ff7bd6d50a99e92b2fa

class Ec_Dif_1():
    def __init__(self) -> None:
        self.x = sympy.Symbol('x')
        self.f = sympy.Function('y')(self.x)
        self.ics = {self.f.subs(self.x, 3): -1}

    def resolver(self):
        eq = ((self.x**2)*(self.f) - self.f) / (self.f + 1)
        dif_eq = sympy.Eq(self.f.diff(self.x), eq)
        sol = sympy.dsolve(dif_eq, ics = self.ics)
        return sol

prueba = Ec_Dif_1()
sympy.init_printing(prueba.resolver())