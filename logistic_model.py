import numpy as np
import matplotlib.pyplot as plt

def logistic_model(a, N, init_x):
    #   N: Iteration step
    #   a: Parameter
    x = init_x
    time = []
    value = []

    for i in range(N):
        time.append(i)
        value.append(x)
        x = a * x * (1 - x)
    return time, value
for a in range(1, 200):
    a = a / 50
    time, value = logistic_model(a, 100, 0.6)
    print(value[99])
    plt.ion()
    plt.plot(time, value, label='a =' + str(a))
    plt.legend()
    plt.pause(0.01)
   
    plt.clf()
plt.ioff()
    
    
