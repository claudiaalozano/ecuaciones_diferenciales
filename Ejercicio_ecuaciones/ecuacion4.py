import sympy as sym
import matplotlib.pyplot as plt
import numpy as np


sym.init_printing(use_latex= True) # Para imprimir en formato LaTeX en la consola 

def resolver():
     y= sym.symbols("f", cls=sym.Function) # Definimos la función f  
     t= sym.symbols("t", real = True)

     eq = sym.Eq(2*t*y(t).diff(t)-y(t), 3*t**2) # Definimos la ecuación diferencial
     a = sym.dsolve(eq) # Resolvemos la ecuación diferencial
     print("La solución a la ecuación 2ty'-y=3t^2 es:")
     sym.pprint(a) # Imprimimos la solución


def ecuacion(t,y):
  dydt = (3*t**2 + y)/2*t
  return dydt
def real(t):
  return t**2 + ((t)**1/2) 


t_0 = 1
y_0 = 3

t_positivo = np.linspace(t_0, 20, 100)
t_negativo = np.linspace(0, t_0, 100)
h= t_positivo[2] - t_positivo[1]

f = [[t_0,y_0]]
f_real = [[t_0, real(t_0)]]

for i,j in enumerate(t_positivo[1:]):
  dydt = ecuacion(f[i][0],f[i][1])
  euler = f[i][1] + dydt*h
  f.append([j, euler])
  f_real.append([j, real(j)])


for i,j in enumerate(list(reversed(t_negativo))[1:]):
  dydt = ecuacion(f[0][0],f[0][1]
  )
  euler = f[0][1] - dydt*h
  f.insert(0,[j, euler])
  f_real.insert(0, [j, real(j)])

t =[i[0] for i in f]
y = [i[1] for i in f]

t_real = [i[0] for i in f_real]
y_real = [i[1] for i in f_real]

plt.figure(figsize=(10,10))
plt.scatter(t, y)
plt.scatter(t_real, y_real)
plt.legend(["Aproximación","Real"])
plt.show()


resolver()


 #def lin():
    # print("\n")

  #   x = symbols("x")
  #   y = symbols("y")
   #  z = symbols("z")
   # t=symbols("t")


    # print(x)
    # print(y)
   #  print(z)
   # print(t)

 #    f = Function("f")("x")
  #   g = Function("g")("y")
 #    M = Function("M")("z")


  #   print(f)
  #   print(g)
  #   print(M)

   #  h=Function("h")
  #   h=h(x,y)
  #   print(h)

     #primera derivada
    # df = diff(f,x)
  #   dg = diff(g,y)
   #  dhx = diff(h,x)
  #   dhy = diff(h,y)

  #   print(df)
   #  lin()

    # print(dg)
    # lin()

    # print(dhx)
   #  lin()

   #  print(dhy)
   #  lin()
 #lin()