# py 3.7
import math
from decimal import Decimal

def mysqrt(a):
    x = a / 2.0
    epsilon = 0.0000001
    while True:
#       print(x)
        y = (x + a/x) / 2
        if math.fabs(y - x) < epsilon:
            break
        x = y
    return x

# print('4: ', mysqrt(4))
# print('9: ', mysqrt(9))
# print('19: ', mysqrt(19))
# print('100: ', mysqrt(100))

def test_square_root(a):
    col_headers = ['a','mysqrt(a)','math.sqrt(a)','diff']

    print('\t'.join(col_headers))

    line = ''
    for header in col_headers:
        line += '-'*len(header)
        line += '\t'
    print(line)
    
    for i in a:
        line = []
        line.append(i)
        line.append(mysqrt(i))
        line.append(math.sqrt(i))
#       print(line[1], " ", line[2], " ", line[1] - line[2])
        line.append(line[1] - line[2])
        line = list(map(str, line))
        for c in range(1, len(col_headers)-1):
            length = len(col_headers[c]) + 3
            if len(line[c]) >= length: line[c] = line[c][0:length]
            else: line[c] = line[c] + ' '*(length - len(line[c])) 
#       print(line)
        print('\t'.join(line))

test_square_root([1,2,3,4,5,6,7,8, 9, 15, 20, 100])

