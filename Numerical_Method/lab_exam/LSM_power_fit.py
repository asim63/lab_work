import numpy as np
import matplotlib.pyplot as plt
import sys
def linear_fit(x,y):
    X = np.array(x)
    Y = np.array(y)
    n = len(X)
    
    sumX = np.sum(X)
    sumY = np.sum(Y)
    sumX2 = np.sum(X**2)
    sumXY = np.sum(X*Y)
    
    d = n* sumX2 - sumX**2
    
    da = sumY * sumX2 - sumXY * sumX
    db = n*sumXY - sumX*sumY
    
    a = da/d
    b = db/d
    print(f"The linear fit is: y = {b}x + {a}")
    return a, b

def power_plot(x_points,y_points,a_log,b):
    x_vals = np.linspace(min(x_points)-1, max(x_points)+1,200)
    a = np.exp(a_log)
    y_vals = a* (x_vals ** b)
    
    plt.figure()
    plt.axhline(0,color='gray', linestyle = 'solid')
    plt.scatter(x_points, y_points, color = 'red', label = 'Data Points')
    plt.plot(x_vals,y_vals, label = "Power Fit",color= 'blue')
    plt.title('Power Fit viz')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()
    
x = [2, 4, 6, 8, 10, 12]
y = [2, 8, 25, 36, 68, 92]   
    
l = len(x)
m = len(y)
if l != m:
    print("Error")
    sys.exit(1)
    
xlog = np.log(x)
ylog = np.log(y)
# power_fit
#y = a* x^b
a_log, b = linear_fit(xlog, ylog)
power_plot(x,y,a_log,b)
