"""
Chapter 13, Exercise 1.2
From Think Python, 2nd Edition
http://greenteapress.com/thinkpython2/html/thinkpython2014.html
---
Exercise 3  

Modify the program from the previous exercise to print the 20 most frequently used words in the book.
"""

import sys
sys.path.append('ch13/')

import ex13_1_1 as wg
import ex13_1_2 as wc

def sort_counts(word_counts):
    """
    This function takes a dictionary of (k,v) pairs where k is the word and v is the number of occurrences. It returns a sorted dictionary that can be enumarted through to see the most frequently occuring words.
    """

    return {k: v for k, v in sorted(word_counts.items(), key=lambda item: item[1], reverse=True)}
            

if __name__ == '__main__':
    plato_counts = wc.word_count_dict(
        wg.read_file('text/ion_pg1635.txt', skiplines=31)
    )

    print("{} unique words found in Plato's ION".format(len(plato_counts)))
    # 1761 unique words found in Plato's ION

    print("Top 20 words:")
    for idx, (k, v) in enumerate(sort_counts(plato_counts).items()):
        print(f'{v}: {k}')
        if idx >= 19: break;
    
    
