import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * np.sin(x) + np.cos(x)

a = float(input("Enter your first guess: "))
b = float(input("Enter your second guess: "))
E = 0.00005

fa = f(a)
fb = f(b)

c = (a*fb - b*fa) / (fb - fa)  # Initial approximation

while abs(f(c)) > E:
    fa = f(a)
    fb = f(b)
    c = (a*fb - b*fa) / (fb - fa)
    a, b = b, c

x = np.linspace(a-10, b+10, 500)
y = f(x)

plt.figure(figsize=(8,5))
plt.axhline(0, color='gray', linestyle='solid')
plt.axvline(c, color='red', linestyle='--', label=f"Root ≈ {c:.5f}")
plt.plot(x, y, label='f(x) = x*sin(x) + cos(x)', color='blue')
plt.scatter(c, f(c), color='red', zorder=5)
plt.title("Secant Method Visualization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
