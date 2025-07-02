import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 4, 5, 7])
y = np.array([1.5, 2.4, 4.1, 5.3, 6.8])
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x * x)

b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - (sum_x) ** 2)
a = (sum_y - b * sum_x) / n

print(f"Best fit line: y = {a:.4f} + {b:.4f}x")
y_pred = a + b * x
plt.figure(figsize=(8, 5), facecolor='white')
plt.scatter(x, y, color='#2ca02c', s=100, edgecolor='k', label='Data Points', zorder=5)
plt.plot(x, y_pred, color='#d62728', linewidth=2.5, label='Least Squares Fit')

plt.title("Least Square Estimation Method", fontsize=16, weight='bold', pad=12)
plt.xlabel("x", fontsize=14, weight='bold')
plt.ylabel("y", fontsize=14, weight='bold')
plt.grid(True, linestyle=':', alpha=0.6) 
plt.text(0.99, 0.01, 'Asim Poudel/08',
         ha='right', va='bottom', transform=plt.gca().transAxes,
         fontsize=12, bbox=dict(facecolor='white', edgecolor='black', pad=4))

plt.legend(fontsize=12, frameon=True, edgecolor='gray')
plt.tight_layout()
plt.show()
