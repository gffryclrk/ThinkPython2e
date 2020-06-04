"""
Chapter 13, Exercise 8.8
From Think Python, 2nd Edition
http://greenteapress.com/thinkpython2/html/thinkpython2014.html
---
Exercise 8  

Markov analysis:

1. Write a program to read a text from a file and perform Markov analysis. The result should be a dictionary that maps from prefixes to a collection of possible suffixes. The collection might be a list, tuple, or dictionary; it is up to you to make an appropriate choice. You can test your program with prefix length two, but you should write the program in a way that makes it easy to try other lengths.
2. Add a function to the previous program to generate random text based on the Markov analysis. Here is an example from Emma with prefix length 2:

    He was very clever, be it sweetness or be angry, ashamed or only amused, at such a stroke. She had never thought of Hannah till you were never meant for me?" "I cannot make speeches, Emma:" he soon cut it all himself. 

    For this example, I left the punctuation attached to the words. The result is almost syntactically correct, but not quite. Semantically, it almost makes sense, but not quite.

    What happens if you increase the prefix length? Does the random text make more sense?
3. Once your program is working, you might want to try a mash-up: if you combine text from two or more books, the random text you generate will blend the vocabulary and phrases from the sources in interesting ways. 

Credit: This case study is based on an example from Kernighan and Pike, The Practice of Programming, Addison-Wesley, 1999.
"""

"""
First, I want to write an iterator that yeilds n words from a file
"""

import string
from collections import deque
import itertools
import pdb

def read_file(filename, n, skiplines=0):
    """
    Returns a function that returns n word generator from input file. 
    """

    def word_generator():
        """
        Creates a generator from filename provided to outer function. Skips specified numebr of lines.

        Generator returns a tuple of two elements: 
        0: Tuple of n words (prefix)
        1: single word suffix
        """
        #TODO: Words at end of text won't be returned if number of words in input file divided by n+1 doesn't have a remainder of 0
        
        wordlist = deque()
        with open(filename) as f:
            for _ in range(skiplines):
                next(f)
            for line in f:
                for word in line.split():
                    wordlist.append(word)
                    if(len(wordlist) == n+1):
                        prefix = tuple(itertools.islice(wordlist, 0, len(wordlist)-1))
                        yield (prefix, wordlist[-1])
                        wordlist.popleft()


    return word_generator()

def build_dict():
    """
    This method uses the read_file() generator to build a dictionary of 
    key, value pairs where the keys are prefixes and the values
    are suffixes
    """

    dict = {}
    word_gen = read_file('./text/emma.txt', n=6, skiplines=249)

    for prefix, suffix in word_gen:
#        I'm changing this to just have a list because the suffix sets seem quite small
#        v = dict.get(prefix, {})
#        v[suffix] = v.get(suffix, 0) + 1
#        dict[prefix] = v
        lst = dict.get(prefix, [])
        lst.append(suffix)
        dict[prefix] = lst

    return dict


if __name__ == "__main__":

#    word_gen = read_file('./text/emma.txt', n=6, skiplines=249)
#    for a in range(1, 12):
#        print("Word {}: {}".format(a, next(word_gen)))

    dict = build_dict()
    print("Dict size: {}".format(len(dict)))

    for k, v in dict.items():
        if len(v) > 1: print("{}, {}".format(k, v))
