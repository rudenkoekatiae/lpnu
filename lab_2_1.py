import math
from math import factorial
a = 0
b = 21
h = 2
def func(x):
    total = 0
    n = 1
    m = 2 * n
    d  = 0.001
    while True:
        f = (x ** m - 1) / factorial(m - 1)
        if (abs(f) < d):
            break
        total += f
        m += 2
    return total    
for i in range(a, b, h):
    x = i / 100
    y = func(x)
    print(f"x={x:.2f}, f(x)={y:.5f}")    
