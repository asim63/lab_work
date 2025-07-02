import numpy as np
import matplotlib.pyplot as plt
x = [1,3,4,5]
y = [3,6,9,12]

fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('My plot')
plt.show()
