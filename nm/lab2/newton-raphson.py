import numpy as np
import matplotlib.pyplot as plt

def f(x): return x * np.sin(x) + x  + np.cos(x) 
def g(x): return x * np.cos(x) + 1

fig, ax = plt.subplots()
x=np.linspace(-10,10,1500)
y=f(x)
ax.plot(x,y,label="f(x)=xsin(x) + x + cos(x)")

# the function is continuous in 4 & 5
a=4.5
b=a-(f(a)/g(a))
error=0.00001
while (abs((b-a)/b)>error):
    a=b
    b=a-(f(a)/g(a))

print("Real root:",b)
ax.set_title("Newton rapshon Method")
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.scatter(b,0,color='red',marker='o', label=f"Approx Root={b}")
plt.legend()
ax.grid()
plt.show()
