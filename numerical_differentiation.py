import numpy as np
import matplotlib.pyplot as plt

def target_function(x):
    y = np.sin(x)
    return y

def objective_function(x): 
    #   Analytical Differentiation.
    y = np.cos(x)
    return y

def numerical_differentiation(start, stop, step):
    X = []                      #    Input
    Y = []                      #    Numerical Gradient
    Y_target = []               #    Target function
    Y_objection = []            #    Objection
  
    for x in np.arange(start, stop, step):
    
        numerical_gradient = (target_function(x) - target_function(x-step)) / step
        
        y_target = target_function(x)
        y_objection = objective_function(x)
        X.append(x)
        Y.append(numerical_gradient)
        Y_target.append(y_target)
        Y_objection.append(y_objection)
    return X, Y, Y_target, Y_objection

start = 0
stop = 2 * 3.14
step = 0.01

X, Y, Y_target, Y_objection = numerical_differentiation(start, stop, step)

plt.figure(0)
plt.scatter(X, Y, label="Numerical Gradient", c='r')
plt.plot(X, Y_target, label="Target Function")
plt.plot(X, Y_objection, label="Objection")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
