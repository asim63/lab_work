import numpy as np
import matplotlib.pyplot as plt
x = [3,4,7,6]
y = [2,4,6,5]

l = len(x)
n = len(y)


def linear_fit(x, y):
    x_points = np.array(x)
    y_points = np.array(y)
    sumx = np.sum(x_points)
    sumy = np.sum(y_points)
    sumX2 = np.sum(x_points**2)
    sumXY = np.sum(x_points * y_points)
    
    d = n*sumX2 - sumx * sumx
    
    da = (sumy * sumX2 - sumXY*sumx)
    
    db = (n*sumXY - sumx * sumy)
    
    a = da /d
    b = db /d
    
    print(f"The linear fit is: y = {b}x + {a}")
    return a, b 


def plot(x_points,y_points,a,b):
    x_vals = np.linspace(min(x_points)-1, max(x_points)+1, 200)
    y_vals = a + b *x_vals
    
    plt.figure()
    plt.axhline(0,color = 'gray', linestyle = 'solid')
    plt.scatter(x_points, y_points, color = 'red', label = 'Data Points')
    plt.plot(x_vals, y_vals,label = 'linear fit', color = "blue")
    plt.title("Linear fit Visualization")
    plt.xlabel("x")
    plt.ylabel("y") 
    plt.legend()
    plt.grid(True)
    plt.show()
    
def ex_plot(x_points,y_points,a_log,b_log):
    x_vals = np.linspace(min(x_points)-1, max(x_points)+1, 200)
    a = np.exp(a_log)
    y_vals =  a * np.exp(b_log*x_vals)
    plt.figure()
    plt.axhline(0,color = 'gray', linestyle = 'solid')
    plt.scatter(x_points, y_points, color = 'red', label = 'Data Points')
    plt.plot(x_vals, y_vals,label = 'linear fit', color = "blue")
    plt.title("Linear fit Visualization")
    plt.xlabel("x")
    plt.ylabel("y") 
    plt.legend()
    plt.grid(True)
    plt.show()
    
if l != n:
    print("Error: The number of x and y points must be the same.")
    
else:

    a ,b = linear_fit(x,y)
    plot(x, y, a, b)
    
    #exponential fit
    ylog = np.log(y)
    a_log, b_log = linear_fit(x, ylog)
    ex_plot(x, y, a_log, b_log)
    

    