import matplotlib.pyplot as plt
import numpy as np
import sympy
from scipy import integrate

x = sympy.Symbol('x')
y = sympy.Function('y')

f = 6*x**2 - 3*x**2*(y(x))
eq = sympy.Eq(y(x).diff(x), f)
print(eq)