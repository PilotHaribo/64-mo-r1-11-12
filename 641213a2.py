from sympy import symbols, solve

# Ungleichung definieren
x = symbols('x')
links = 9 * (x**3 + x)
rechts = 2 * (x**2 + x + 1)**2

# Ungleichung Lösen
lösung = solve(links - rechts <= 0, x)

# Lösung ausgeben
print(lösung)