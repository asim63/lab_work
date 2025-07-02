import numpy as np
import matplotlib.pyplot as plt
import math
x_vals = np.array([1, 2, 3, 4, 5])
y_init = np.array([-9, 1, 35, 105, 223])
n = len(x_vals)
d = np.zeros((n, n))
d[:, 0] = y_init  
for i in range(1, n):
    for j in range(n - i):
        d[j][i] = d[j + 1][i - 1] - d[j][i - 1]
print("Forward Difference Table:")
for i in range(n):
    print(f"{x_vals[i]:.2f}", end="\t")
    for j in range(n - i):
        print(f"{d[i][j]:.2f}", end="\t")
    print()
x = 3.3  
x0 = x_vals[0]
h = x_vals[1] - x_vals[0]  
p = (x - x0) / h
value=d[0][0]
P=1
for i in range(1,n):
    P*=(p-i+1)
    value += (P*d[0][i])/math.factorial(i)
print(f"\nInterpolated value at x = {x} is {value}")
fig, ax = plt.subplots()
ax.set_title('Newton Forward Difference Interpolation')
ax.set_xlabel('x')  
ax.set_ylabel('f(x)')
ax.plot(x_vals, y_init, 'bo-', label='Original Data')
ax.scatter(x, value, color='red', marker='o', label=f"Interpolated Value at x={x}")
ax.legend()
plt.grid(True)
plt.show()
