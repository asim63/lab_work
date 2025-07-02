import numpy as np
import matplotlib.pyplot as plt


f=lambda x: x**3-5*(x)-2

# for i in range(10):
#     print(i,f(i))

fig, ax = plt.subplots()
x=np.linspace(-5,5,1200)
y=f(x)
ax.plot(x,y)

# f(x) is continuous at interval [1,2]

a=0
b=-1
error=0.00001
while (abs(b-a)>error):
    c=(a+b)/2
    if(f(c)>0):
        b=c
    else:
        a=c
    ax.scatter(c,0,color='green',marker='o')


print("Real root:",c)

ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.scatter(c,0,color='red',marker='x')
ax.grid()
plt.show()

