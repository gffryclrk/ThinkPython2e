"""
Chapter 13, Exercise 1.2
From Think Python, 2nd Edition
http://greenteapress.com/thinkpython2/html/thinkpython2014.html
---
An alternative is:

    Use keys to get a list of the words in the book.
    Build a list that contains the cumulative sum of the word frequencies (see Exercise 2). The last item in this list is the total number of words in the book, n.
    Choose a random number from 1 to n. Use a bisection search (See Exercise 10) to find the index where the random number would be inserted in the cumulative sum.
    Use the index to find the corresponding word in the word list.

Exercise 7  

Write a program that uses this algorithm to choose a random word from the book. Solution: http://thinkpython2.com/code/analyze_book3.py.

"""

import sys
sys.path.append('ch13/')

import ex13_1_1 as wg
import ex13_1_2 as wc
from cumsum import cumsum
from ex13_1_3 import sort_counts

import random
from scipy.stats import chisquare

def sort_hist_to_list(word_dict):
    """
    In order to be able to complete the above I need not a sorted dictionary, as I originally implemented (although perhaps this could be done with items()? 
    """
    return [(k, v) for k, v in sorted(word_dict.items(), key=lambda item: item[1], reverse=True)]

def binary_search_leftmost(a, n, t):
    """
    I wasn't able to get my bisect_index_search() function to work
    and so discovered this much simpler algorithm on Wikipedia
    """
    l = 0
    r = n
    while l < r:
        m = (l + r) // 2
        if a[m] < t:
            l = m + 1
        else:
            r = m

    return l
    
if __name__ == '__main__':

    
    emma_counts = wc.word_count_dict(
            wg.read_file('../text/emma.txt', skiplines=249)
    )

    sorted_emma_counts_list = sort_hist_to_list(emma_counts)

    print("sorted emma counts:")
    for t in zip(range(10), sorted_emma_counts_list):
        print(t)

    emma_frequency_list = [x[1] for x in sorted_emma_counts_list]
    
    sorted_emma_cumsum = cumsum(emma_frequency_list)

    assert sum(emma_counts.values()) == sorted_emma_cumsum[-1]

    sampled_from_distribution = {}
    for i in range(1, sorted_emma_cumsum[-1]):
        rand_n = random.randint(0, sorted_emma_cumsum[-1])
        rand_word = sorted_emma_counts_list[binary_search_leftmost(sorted_emma_cumsum, len(sorted_emma_cumsum), rand_n)][0]

        sampled_from_distribution[rand_word] = sampled_from_distribution.get(rand_word, 0) + 1

    sorted_random_sample_list = sort_hist_to_list(sampled_from_distribution)
    print("sorted randomly generated from emma distribution counts:")

    for t in zip(range(10), sorted_random_sample_list):
        print(t)

    sample_frenquency_list = [sampled_from_distribution.get(k[0], 0) for k in sorted_emma_counts_list]

    """
    Chisquare test to see if the algorith is working...
    Usually insufficient evidence
    """
    chisq = chisquare(sample_frenquency_list[:10], f_exp=emma_frequency_list[:10])
    print("H_0: Probabilities of 10 most frequent sampled words are the same as observed")
    print("H_a: At least one of the probabilities of top 10 sampled words is different")
    print("Sufficient evidence to reject H_0: {} (p < 0.05)".format(chisq[1] < 0.05))    
        
