"""
From Think Python, 2nd Edition
http://greenteapress.com/thinkpython2/html/thinkpython2011.html#cumulative

Chapter 10
Exercise 2  

Write a function called cumsum that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i+1 elements from the original list. For example:

>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
"""

def cumsum(t):
    cumsum = []
    total = 0
    for e in t:
        total += e
        cumsum.append(total)

    return cumsum


if __name__ == '__main__':
    t = [1, 2, 3]
    print(cumsum(t))
