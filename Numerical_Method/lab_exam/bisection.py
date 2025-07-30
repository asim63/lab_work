import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x*np.sin(x) + np.cos(x)

def ask_values():
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    return a, b

a,b = ask_values()
    
while (f(a) * f(b) >= 0):
    print("The function has the same sign at the endpoints a and b.")
    a, b = ask_values()
    
    
def bisection(a, b):
    c = (a+b)/2
    E = 0.00005

    while(f(c) != 0 and abs(f(c)) > E):
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
        
    print(f"The root is approximately: {c}")
    print(f"f({c}) = {f(c)}")

    x = np.linspace(a - 1, b + 1, 500) 
    y = f(x)

    plt.figure(figsize=(8, 5))
    plt.axhline(0, color='gray', linestyle="solid")  # x-axis
    plt.axvline(c, color='red', linestyle='--', label=f'Root ≈ {c:.4f}')  # root line
    plt.plot(x, y, label='f(x) = x*sin(x) + cos(x)', color='blue')
    plt.scatter(c, f(c), color='red', zorder=5)

    plt.title("Bisection Method Visualization")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()
    

# bisection(a, b)

for i in range(0,20):
    j= i + 1
    if( f(i) * f(j) < 0):
        bisection(i, j)