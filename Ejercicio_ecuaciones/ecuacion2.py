import sympy as sym
sym.init_printing(use_latex= True)
y = sym.symbols("f", cls=sym.Function)
x = sym.symbols("x", real = True)

eq = sym.Eq(y(x).diff(x)*sym.sin(x), y(x) * sym.log(y(x)))
a = sym.dsolve(eq, ics ={y(sym.pi/2): sym.exp(1), sym.diff(y(x), x).subs(x, sym.pi/2): sym.exp(1)})
print("La solución a la ecuación y`sen(x) = y ln(y) es:")
sym.pprint(a)


#def lin():
   # print("\n")

 #   x = symbols("x")
 #   y = symbols("y")
  #  z = symbols("z")
    

   # print(x)
   # print(y)
  #  print(z)

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