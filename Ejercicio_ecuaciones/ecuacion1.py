import numpy 
import matplotlib.pyplot as plt
from scipy import integrate
from sympy import O

def f(y,x):
    return (x**2*y-y)/(y+1)

y0= 1.0
x= numpy.linspace(0,1,100) # esto sirve para crear un vector de 100 puntos entre 0 y 1

sol= integrate.odeint(f,y0,x) # esto es para resolver la ecuacion diferencial