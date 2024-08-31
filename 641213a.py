import sympy as sp

# Variable definieren
x = sp.symbols('x')

# Ausdruck
term = (x**2 + x + 1)**2

# Klammern auflösen
ausmultiplizierter_term = sp.expand(term)
print("Ausmultiplizierter Term: ")
print(ausmultiplizierter_term)

# Polynom definieren
x = sp.symbols('x')
polynomial = -x**4 + 2.5*x**3 - 3*x**2 + 2.5*x - 1

# Nullstellen berechnen
ns = sp.solve(polynomial, x)
print("Nullstellen: ")
print(ns)

# Prüfen für x aus dem Intervall x < 1
x_null = polynomial.subs(x, 0)
print("Für x = 0 ergibt sich: ")
print(x_null)
if x_null < 1:
    print("Ungleichung ist für x < 1 erfüllt")

# Prüfen für x aus dem Intervall x >= 1
x_zwei = polynomial.subs(x, 2)
print("Für x = 2 ergibt sich: ")
print(x_zwei)
if x_zwei < 1:
    print("Ungleichung ist für x >= 1 erfüllt")