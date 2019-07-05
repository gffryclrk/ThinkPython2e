"""
Exercise 2  

Read the documentation of the dictionary method setdefault and use it to write a more concise version of invert_dict. Solution: http://thinkpython2.com/code/invert_dict.py. 
"""

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, list()).append(key)
    return inverse

hist = {'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
print(invert_dict(hist))
