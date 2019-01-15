"""
Recurse function from Think Python, 2nd ed, Chapter 5 Exercise 4

Functions takes two integers, n and s, and recursively calls itself while decrementing the value of n by one while increasing the value of s by the current value of s in the stack. The base case of recursion is when n reaches 0, which will result in the value of s being printed. Calling the function with a negative value of n will result in error.
"""


def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)
