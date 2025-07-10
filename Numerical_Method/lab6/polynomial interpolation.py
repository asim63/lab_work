import numpy as np
import matplotlib.pyplot as plt

def construct_matrix(x):
    n = len(x)
    A = [[x[i]**(n - j - 1) for j in range(n)] for i in range(n)]
    return np.array(A, dtype=float)

def cramer_rule_solver(A, y):
    n = len(y)
    det_A = np.linalg.det(A)
    if np.isclose(det_A, 0):
        raise ValueError("System matrix is singular.")
    
    coeffs = []
    for i in range(n):
        A_temp = A.copy()
        A_temp[:, i] = y
        coeffs.append(np.linalg.det(A_temp) / det_A)
    return coeffs

def format_polynomial(coeffs):
    terms = []  
    degree = len(coeffs) - 1
    for i, coef in enumerate(coeffs):
        power = degree - i
        if np.isclose(coef, 0):
            continue
        if coef < 0:
            sign = "- "
            coef = -coef
        else:
            sign = "+ " if terms else ""

        if power == 0:
            terms.append(f"{sign}{coef:.2f}")
        elif power == 1:
            terms.append(f"{sign}{coef:.2f}x")
        else:
            terms.append(f"{sign}{coef:.2f}x^{power}")
    return " ".join(terms)

x_vals = [1, 2, 4, 5, 7]
y_vals = [2, 3, 5, 8, 10]

A = construct_matrix(x_vals)
coefficients = cramer_rule_solver(A, y_vals)
poly_str = format_polynomial(coefficients)

print(f"Fitted Polynomial (degree {len(coefficients)-1}):")
print(f"y = {poly_str}")

x_plot = np.linspace(min(x_vals), max(x_vals), 200)
y_plot = np.polyval(coefficients, x_plot)

plt.figure(figsize=(6, 4))
plt.scatter(x_vals, y_vals, color='red', label='Data Points')

for xi, yi in zip(x_vals, y_vals):
    plt.text(xi, yi, f"({xi}, {yi})", fontsize=8, ha='right')

plt.plot(x_plot, y_plot, color='blue', label=f'y = {poly_str}')
plt.title('Asim's Polynomial Curve Fitting')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
