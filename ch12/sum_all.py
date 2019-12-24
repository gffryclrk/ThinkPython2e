"""
http://greenteapress.com/thinkpython2/html/thinkpython2013.html
As an exercise, write a function called sum_all that takes any number of arguments and returns their sum.
"""

def sum_all(*args):
    sum = 0
    for a in args:
        if type(a) is not int: continue
        sum += a

    return sum

print("sum of 1, 2, 3: {}".format(sum_all(1, 2, 3)))    
print("sum of 1, 2, 3, a: {}".format(sum_all(1, 2, 3, 'a')))    
