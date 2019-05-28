import math
import itertools

def estimate_pi():
    const = 2  * math.sqrt(2) / 9801

    x = itertools.count() 
    sum = 0
    while True:
        k = next(x)    
        this_k = math.factorial(4 * k) * (1103 + (26390 * k)) / ((math.factorial(k) ** 4 ) * ( 396 ** (4 * k))) 
        print(this_k)
        sum += this_k

        if this_k < float('1e-15'): break

    print(sum * const)

estimate_pi()
