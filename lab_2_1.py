import math
from math import factorial

def func(x):
    total = 0
    n = 1
    m = 2 * n
    while True:
        f = (x ** m - 1) / factorial(m - 1)
        if (abs(f) < 0.001):
            break
        total += f
        m += 2
    return total
    
for i in range(0, 21, 2):
    x = i / 100
    y = func(x)
    print(f"x={x:.2f}, f(x)={y:.5f}")    