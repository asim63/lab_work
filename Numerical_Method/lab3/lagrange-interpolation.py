import numpy as np
import matplotlib.pyplot as plt
def lagrange_interpolation(x_val, y_val, unknown_x):
    n = len(x_val)
    result = 0

    for i in range(n):
        term = y_val[i]
        for j in range(n):
            if i != j:
                term *= (unknown_x - x_val[j]) / (x_val[i] - x_val[j])
        result += term
    return result
x = [5, 6, 9, 11]
y = [12, 13, 14, 16]

x_interp = 8
y_interp = lagrange_interpolation(x, y, x_interp)
print(f"f({x_interp}) ≈ {y_interp:.4f}")

x_data = np.linspace(4, 12, 1600)
y_data = [lagrange_interpolation(x, y, xx) for xx in x_data]

plt.plot(x_data, y_data, label="Interpolated Curve")
plt.scatter(x, y, color='blue', label="Data Points")
plt.scatter(x_interp, y_interp, color='red', label=f"f({x_interp})")
plt.legend()
plt.grid()
plt.title("Lagrange Interpolation (Asim BCT008) ")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
