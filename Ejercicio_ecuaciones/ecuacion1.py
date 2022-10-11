from sympy import *

def resolver():
    x= Function('x')
    y= Function('y')
    
    edo= Eq(diff(y(x)),(x**2*y-y)/(y + 1))
    CI={y(3):1}
    dsolve(edo,y(x),ics=CI)




