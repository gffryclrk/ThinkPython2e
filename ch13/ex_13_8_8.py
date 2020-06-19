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
import sys
sys.path.append('ch13/')
import ex_13_7_7 as ex13_7

from cumsum import cumsum

import string
from collections import deque
import itertools
import random
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

def build_dict(prefix_length=2):
    """
    This method uses the read_file() generator to build a dictionary of 
    key, value pairs where the keys are prefixes and the values
    are suffixes
    """

    dict = {}
    word_gen = read_file('../text/emma.txt', n=prefix_length, skiplines=249)

    for prefix, suffix in word_gen:
        v = dict.get(prefix, {})
        v[suffix] = v.get(suffix, 0) + 1
        dict[prefix] = v

    return dict

def build_organized_dict(dict):
    """
    This function takes unorganized parse of corpus,
    which is (k,v) = (prefix: {suffix: count})
    and transforms it to (k,v) = (prefix: {"suffixes": [], "frequences": []}),
    where 'suffixes' is an ordered list of suffixes in descding order of frequency
    and 'frequencies' is a cumulative sum of frequencies of the suffix in the same
    list position. 
    """

    ordered_dict = {}
    for k,v in dict.items():
        sorted_v_list = ex13_7.sort_hist_to_list(v)
        sorted_freq_list = [x[1] for x in sorted_v_list]
        sorted_word_list = [x[0] for x in sorted_v_list]
        ordered_dict[k] = {'suffixes': sorted_word_list, 'frequencies': cumsum(sorted_freq_list)}
        

    return ordered_dict
def choose_suffix(prefix, ordered_dict):
    """
    This function takes a prefix and ordered dictionary and 
    randomly chooses a suffix with probability in proportion
    to its number of appearances in the input corpus.
    """

    v = ordered_dict[prefix]
    rand_n = random.randint(0, v['frequencies'][-1])
    rand_word_index = ex13_7.binary_search_leftmost(v['frequencies'], len(v['frequencies']), rand_n)
    
    return v['suffixes'][rand_word_index]

def choose_n_words(ordered_dict, beginning, n=10):
    """
    This function chooses words from the Markov chain
    @param ordered_dict - dictionary in proper format
    @param beginning - tuple to 'prime the pump'
                       This value is also used judge the length of prefix
    @param n - Number of words to generate
    """
    
    def choose_word(frequencies, suffixes):
        """
        Choose random word proportionally from given frequency & suffix lists
        """

        rand_n = random.randint(0, frequencies[-1])
        rand_word_index = ex13_7.binary_search_leftmost(frequencies, len(frequencies), rand_n)
        rand_word = suffixes[rand_word_index]
        return rand_word

    
    output = list(beginning)
    prefix_length = len(beginning)
    while len(output) < (n + prefix_length):
        pdb.set_trace()
        word = choose_word(ordered_dict[beginning]['frequencies'], ordered_dict[beginning]['suffixes'])
        new_prefix = tuple(output[-(prefix_length -1 ):] + [word])
        old_prefix = tuple(output[-(prefix_length):])
        if new_prefix in ordered_dict:
            output.append(word)
        elif len(ordered_dict[old_prefix]['suffixes']) == 1:
            raise ValueError(f"Combination of generated suffixes has made it impossible to proceed: {output}")


    return output

        

if __name__ == "__main__":
  dict = build_dict(4)
  print("Dict size: {}".format(len(dict)))



  ordered_dict = build_organized_dict(dict)

  most_suffixes = max(ordered_dict.items(), key = lambda x: x[1]['frequencies'][-1])

  print(f"Most suffixes found for {most_suffixes} with {most_suffixes[1]['frequencies'][-1]}")
    
  choose_n_words(ordered_dict, most_suffixes[0], 10)
      

  
  
