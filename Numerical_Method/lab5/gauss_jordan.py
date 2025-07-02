import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gauss_jordan(A, b):
    n = len(b)
    AugmentedMatrix = np.hstack([A, b.reshape(-1, 1)])
    
    # Perform Gauss-Jordan elimination
    for i in range(n):
        # Normalize the pivot row
        AugmentedMatrix[i] = AugmentedMatrix[i] / AugmentedMatrix[i, i]
        
        # Eliminate other rows
        for j in range(n):
            if i != j:
                AugmentedMatrix[j] = AugmentedMatrix[j] - AugmentedMatrix[j, i] * AugmentedMatrix[i]

    return AugmentedMatrix[:, -1]

# Example system of equations:
# 3x - 2y + z = 2
# x + 3y + 2z = 8
# 2x + y + z = 5

A = np.array([[3, -2, 1], [1, 3, 2], [2, 1, 1]], dtype=float)
b = np.array([2, 8, 5], dtype=float)

solution = gauss_jordan(A, b)
print("Solution:", solution)

# Plotting the planes:
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create grid for plotting
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)

# Equations for the planes (solving for Z)
Z1 = (2 - 2*X + Y) / 1
Z2 = (12 - X - 3*Y) / 2
Z3 = 5 - X - Y

# Plot the planes
ax.plot_surface(X, Y, Z1, alpha=0.5, rstride=100, cstride=100, color='r')
ax.plot_surface(X, Y, Z2, alpha=0.5, rstride=100, cstride=100, color='g')
ax.plot_surface(X, Y, Z3, alpha=0.5, rstride=100, cstride=100, color='b')

# Labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()
