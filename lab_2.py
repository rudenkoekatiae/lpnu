import math
from math import log, cos

def func(x):
    try:
        if x < 5:
            return log(abs(log(abs(log(x)) / log(3))) / log(4)) / log(5)
        elif x >= 5 and x < 7:
            return 1 / (x * x + 16)
        elif x >= 7:
            return log(x) + cos(x)
    except ValueError:
        return None
    
a = 3
b = 8.0
h = 0.2
x = a
tolerance = 1e-9
while x <= b + tolerance:
    y = func(x)
    if y is not None:
        print(f"x = {x:.2f}, f(x) = {y:.5f}")
    else:
        print("Value Error")
    x += h