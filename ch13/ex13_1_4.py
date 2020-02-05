"""
Chapter 13, Exercise 1.2
From Think Python, 2nd Edition
http://greenteapress.com/thinkpython2/html/thinkpython2014.html
---
Exercise 4

Modify the previous program to read a word list (see Section 9.1) and then print all the words in the book that are not in the word list. How many of them are typos? How many of them are common words that should be in the word list, and how many of them are really obscure?
"""

import sys
sys.path.append('ch13/')

import ex13_1_1 as wg
import ex13_1_2 as wc
            

if __name__ == '__main__':
    """
    There are 210 words that aren't in the word dictionary. Some are names and proper nouns, such as achilles. Some entries are numbers, some are words that were smashed together after punction was removed (navigation--will => navigationwill), and some are entries from the copyright/info footer such as httpwwwgutenbergorg). 

    There are perhaps also some words that aren't in the dictionary, such as merchantibility. This is a translated book, afterall.

    I'm sufficiently happy with this solution and don't see any reason to add logic to fix the above issues.
    """
    
    plato_words = {}
    for word in wg.read_file('text/ion_pg1635.txt', skiplines=31):
        plato_words[word.lower()] = ''

    print("{} unique plato_words found in Plato's ION".format(len(plato_words)))
    # 1761 unique plato_words found in Plato's ION

    dictionary_words = {}
    for word in wg.read_file('text/words.txt', skiplines=0):
        dictionary_words[word.lower()] = ''

    word_diff = set(plato_words.keys()) - set(dictionary_words.keys())

    print("{} Words found in Plato's ION which are not in the words.txt dictionary:".format(len(word_diff)))
    for word in word_diff:
        print(word)
