"""
Think Python, 2nd ed
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

Chapter 14.5 in-line exercise
The os module provides a function called walk that is similar 
to this one but more versatile. As an exercise, read the 
documentation and use it to print the names of the files in a 
given directory and its subdirectories.
"""
import os
import sys
import pdb

def recursive_walk(path):
    """ A method to walk recursively through directories """
    # pdb.set_trace()
    walker = os.walk(path)
    for contents in walker:
        print('\n'.join(contents[2]))
        for subdir in contents[1]:
            recursive_walk(f'{path}{subdir}')


if __name__ == '__main__':
    """Run this program from the command line using:
 
    $ python3 ex_14_4_walk.py <path>
   
    Where <path> is the path to a directory to be recursively printed.
    """
    
    path = sys.argv[1]

    print(f'Walking path {path}')
    recursive_walk(path)

