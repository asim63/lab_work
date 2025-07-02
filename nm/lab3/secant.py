import numpy as np
import matplotlib.pyplot as plt

f=lambda x: x**4-(x)-2

fig, ax = plt.subplots()
x=np.linspace(-20,20,1600)
y=f(x)
ax.plot(x,y,label="f(x)=x^4-x-2")

# the function is continuous in 1 & 2
a=1
b=2
error=0.00001
while (abs(b-a)>error):
    c=(a*f(b)-b*f(a))/(f(b)-f(a))
    a=b
    b=c

print("Real root:",c)
ax.set_title('Secant (Asim BCT008)')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.scatter(b,0,color='red',marker='x', label=f"Approx Root={b}")
plt.legend()
ax.grid()
plt.show()
