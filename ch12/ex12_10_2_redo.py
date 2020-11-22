""" Think Python, 2nd ed
Chapter 12, Exercise 2

I originally (partially) solved ex12.10.2 in ex12_10_2.py, however
when I revisited the code to import it as a module for exercise
14.12.2 it was a mess. As a result I'm re-writing it and re-facoring
where necessary here.
"""
import string
import pdb

def word_gen(path, skiplines=0):
    """Similar to ex_13_7_7, I would like to use a generator 
    to read the file.
    
    In order to simplify custom hashing using prime multipltiplication punctuation is stripped. This is not a parameter. 

    The string is also being converted to lowercase before being returned for compatability with hashing
    """

    with open(path) as f:
        for _ in range(skiplines):
            next(f)
        for line in f:
            stripped_line = line.translate(str.maketrans('', '', string.punctuation+string.digits))
            for word in stripped_line.split():
                yield word.lower()


def custom_hash(str_in):
    """This hash function uses the fundamental theorem of arithmatic to 
    generate a hash. This toy implementation only works on lowercase letters.
    <https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic> """
    
    PRIMES = [
        2, 3, 5, 7, 11, 13,
        17, 19, 23, 29, 31,
        37, 41, 43, 47, 53,
        59, 61, 67, 71, 73,
        79, 83, 89, 97, 101
        ]

    LOWERCASE_Z_ASCII = ord('z')
    hash_count = 1

    for letter in str_in:
        try:
            hash_count *= PRIMES[ord(letter) - LOWERCASE_Z_ASCII]
        except IndexError:
            print(f'list index out of range: {letter} in {str_in}')
     
    return hash_count

def build_anagram_dict(word_gen, starting_dict={}, hash_fn=lambda x: tuple(sorted(x))):
    """This is also based largely on the ex_13_7_7 solution.
    This method returns a reference to the dictionary which was 
    updated or created. 
    """

    dict = starting_dict

    for word in word_gen:
        key = hash_fn(word)
        word_list = dict.get(key, {})
        #TODO: Using list as dict value will result in duplicates, consider hash table
        word_list[word] = None
        dict[key]= word_list

    return dict

    
if __name__ == '__main__':
    """Write a program that reads a word list from a file (see Section
    9.1) and prints all the sets of words that are anagrams."""

    emma_gen = word_gen("text/emma.txt")
    dict = build_anagram_dict(emma_gen)

    # Modify the previous program so that it prints the longest list
    # of anagrams first, followed by the second longest, and so on.
    dictlen = {k:len(v) for (k,v) in dict.items()}
    """max(dictlen, key=dictlen.get)
    ('e', 'h', 'o', 's', 't')
    >>> dictlen[('e', 'h', 'o', 's', 't')]
    3
    >>> dict[('e', 'h', 'o', 's', 't')]
    {'those': None, 'sothe': None, 'sheto': None}"""

    it = iter(sorted(dictlen, key=dictlen.__getitem__, reverse=True))
    """
    >>> next(it)
    ('e', 'h', 'o', 's', 't')
    """
    
