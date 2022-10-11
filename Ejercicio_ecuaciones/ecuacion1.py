import sympy

class Ec_Dif_1():
    def __init__(self) -> None:
        self.x = sympy.Symbol('x')
        self.f = sympy.Function('y')(self.x)

    def resolver(self):
        eq = ((self.x**2)*(self.f) - self.f) / (self.f + 1)
        dif_eq = sympy.Eq(self.f.diff(self.x), eq)
        sol = sympy.dsolve(dif_eq)
        return sol