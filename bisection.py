import numpy as np

def func(x):
    y = x**2 + x - 1
    return y

acc = 0.001
a = 1
upper = 1
lower = 0
while abs(a) > acc:
    a = func((upper + lower) / 2)
    print(a, lower, upper)

    if a > 0:
        upper = (upper + lower) / 2
    else:
        lower = (upper + lower) / 2

    
