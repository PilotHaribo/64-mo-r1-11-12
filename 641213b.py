import numpy as np
import matplotlib.pyplot as plt

# Define functions for the left and right-hand sides of the inequality
def lhs_func(x, y):
    return 9 * (x**3 * y + x * y**3)

def rhs_func(x, y):
    return 2 * (x**2 + x * y + y**2)**2

# Generate grid values for x and y
x_vals = np.linspace(-2, 2, 400)
y_vals = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x_vals, y_vals)

# Compute the left and right-hand side values on the grid
lhs_vals = lhs_func(X, Y)
rhs_vals = rhs_func(X, Y)

# Plotting the inequality (lhs ≤ rhs) using contours
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, lhs_vals - rhs_vals, levels=[-1e9, 0], colors=['#00bfff', '#ff6666'], alpha=0.7)
plt.colorbar(label='Difference (lhs - rhs)')
plt.title('Inequality: $9(x^3 y + x y^3) \leq 2 (x^2 + x y + y^2)^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
