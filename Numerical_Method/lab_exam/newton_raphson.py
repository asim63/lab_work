import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*np.sin(x) + np.cos(x)
def df(x):
    return x*np.cos(x) 



a = int(input("Enter your initial guess: "))
E = 0.00005
c = a - f(a) / df(a)
while(not df(c) ==0 and  abs(f(c)) > E):

    c = a - f(a) / df(a)
    a = c
print(f"The root is approximately: {c}")

x = np.linspace(a-10, a+10, 500)
y = f(x)

plt.figure(figsize = (8,5))
plt.axhline(0, color = 'gray', linestyle = 'solid')
plt.axvline(c, color = 'red', linestyle = '--', label = f"Root = {c:.4f}")
plt.plot(x,y,label = 'f(x) = x*sin(x) + cos(x)', color = 'blue')
plt.scatter(c, f(c), color = 'red', zorder = 5)
plt.title("Newton-Raphson Method Visualization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
