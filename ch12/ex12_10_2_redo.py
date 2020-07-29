"""I originally (partially) solved ex12.10.2 in ex12_10_2.py, however
when I revisited the code to import it as a module for exercise
14.12.2 it was a mess. As a result I'm re-writing it and re-facoring
where necessary here.
"""

import pdb

def word_gen(path, skiplines=0):
    """Similar to ex_13_7_7, I would like to use a generator to read the file"""

    with open(path) as f:
        for _ in range(skiplines):
            next(f)
        for line in f:
            for word in line.split():
                yield word


def build_anagram_dict(word_gen, starting_dict={}):
    """This is also based largely on the ex_13_7_7 solution.
    This method returns a reference to the dictionary which was updated or created. 
    """

    dict = starting_dict

    for word in word_gen:
        key = tuple(sorted(word))
        word_list = dict.get(key, [])
        dict[key] = word_list + [word]

    return dict

    
if __name__ == '__main__':
    """Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of words that are anagrams."""

    emma_gen = word_gen("text/emma.txt")
    dict = build_anagram_dict(emma_gen)

    # Lifting this from my original solution
    # Below needs work...
#    sorted_angram_lengths = [k for (k, v) in sorted(lengths.items(), key = lambda item: len(item[1]), reverse=True)]
    
