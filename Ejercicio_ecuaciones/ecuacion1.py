import sympy
import sys
import pprint

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