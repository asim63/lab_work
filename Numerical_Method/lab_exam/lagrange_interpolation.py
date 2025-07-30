import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_points,y_points, x):
    total = 0
    n = len(x_points)
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if j != i:
                term = term * (x - x_points[j])/(x_points[i] - x_points[j])
        total += term
    return total


x_points = [3,4,7,6]
y_points = [2,3,4,2]

x_vals = np.linspace(min(x_points)-1, max(x_points)+1, 200)
y_vals = []

for x in x_vals:
    y_vals.append(lagrange_interpolation(x_points,y_points,x))

plt.figure(figsize= (8,5))
plt.axhline(0, color = 'gray', linestyle = 'solid')
plt.scatter(x_points, y_points, color = 'red', zorder = 5, label = 'Data Points')
plt.plot(x_vals,y_vals, label = "lagrange Interpolation", color = 'blue')
plt.title("Lagrange Interpolation Visualization")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()    
plt.show()
