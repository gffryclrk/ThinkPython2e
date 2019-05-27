# py 2.7
import math

def mysqrt(a):
    x = a / 2
    epsilon = 0.00001
    while True:
        print(x)
        y = (x + a/x) / 2
        if math.fabs( y - x) < epsilon:
            break
        x = y
    return x

print('4: ', mysqrt(4))
print('9: ', mysqrt(9))
print('19: ', mysqrt(19))
print('100: ', mysqrt(100))
