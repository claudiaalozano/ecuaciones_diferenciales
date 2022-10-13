import sympy as sym
sym.init_printing(use_latex= True) # Para imprimir en formato LaTeX en la consola 

def resolver_3():
    y= sym.symbols("f", cls=sym.Function) # Definimos la función f  
    t= sym.symbols("t", real = True) # Definimos la variable t

    eq = sym.Eq(y(t).diff(t)-y(t)/(t-2), 2*(t-2)**2) # Definimos la ecuación diferencial
    a = sym.dsolve(eq) # Resolvemos la ecuación diferencial
    print("La solución a la ecuación y'- (y/(t-2))= 2(t-2)^2 es:")
    sym.pprint(a) # Imprimimos la solución

resolver_3()

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