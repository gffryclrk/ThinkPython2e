"""
As an exercise, type this example into a file named wc.py and run
it as a script. Then run the Python interpreter and import wc. What is
the value of __name__ when the module is being imported?

>>> sys.path.append('ch14')
>>> import ex_14_9_wc as wc
__name__: ex_14_9_wc
"""

def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

if __name__ == '__main__':
    print(linecount('wc.py'))
else:
    print(f'__name__: {__name__}')

