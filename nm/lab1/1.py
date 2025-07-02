#x =1 
#y = 2*x + 1
#print(y)

# f = lambda x: 2*x + 1
# print(f(1))

# print(list(map(f,[1,2,3])))
# print(list(map(f, range(5))))

import numpy as np
f = lambda x:2*x + 1
print(f(np.arange(5)))
