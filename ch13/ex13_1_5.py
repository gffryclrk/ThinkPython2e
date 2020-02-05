"""
Chapter 13, Exercise 1.2
From Think Python, 2nd Edition
http://greenteapress.com/thinkpython2/html/thinkpython2014.html
---
Exercise 5  

Write a function named choose_from_hist that takes a histogram as defined in Section 11.2 and returns a random value from the histogram, chosen with probability in proportion to frequency. For example, for this histogram:

>>> t = ['a', 'a', 'b']
>>> hist = histogram(t)
>>> hist
{'a': 2, 'b': 1}

your function should return 'a' with probability 2/3 and 'b' with probability 1/3. 

"""

import ch11_histogram as hst

import random


def naive_weighted_list(histogram):
    """
    This solution is pretty simple because, apparently, since v. 3.6 the random package has a .choices() method that accepts weights as an argument: https://docs.python.org/3/library/random.html#random.choices
    It would be too easy to use this implementation so I took the naive approach and implemented this function which creates a list of letters to choose from. 
    """
    l = []
    for k, v in histogram.items():
        l += [k] * v

    return l
        
if __name__ == "__main__":
    bronto_histo = hst.histogram('brontosaurus')
    bronto_listo = naive_weighted_list(bronto_histo)

    print("histogram of brontosaurus: {}\nlist with appropriate elements: {}\nrandom selection: {}".format(bronto_histo, bronto_listo, random.choice(bronto_listo)))
    
    

