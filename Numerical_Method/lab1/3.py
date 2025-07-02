import numpy as np
import matplotlib.pyplot as plt

n = 100
x = np.arange(1,n)

fig, ax = plt.subplots()
for i in range(5):
    ax.plot(x, pow(x,i), label='$x^{}$'.format(i))
ax.grid()
ax.legend()
ax.set_xlim(0, n)
ax.set_ylim(0, n)
plt.show()
