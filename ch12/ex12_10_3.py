"""
Exercise 3  

Two words form a “metathesis pair” if you can transform one into the other by swapping two letters; for example, “converse” and “conserve”. Write a program that finds all of the metathesis pairs in the dictionary. Hint: don’t test all pairs of words, and don’t test all possible swaps. Solution: http://thinkpython2.com/code/metathesis.py. Credit: This exercise is inspired by an example at http://puzzlers.org.
"""

import pdb
import itertools

def anagram_dict(filename):
    anagrams = {}
    for line in open(filename):
        word = line.strip()
        key = tuple(sorted(word))
        anagram_list = anagrams.get(key, [])
        anagram_list.append(word)
        anagrams[key] = anagram_list
    
    return anagrams
    
def check_meta_pair(s1, s2):
    """
    This function takes two anagrams and returns a boolean of whether they are metathesis pairs
    """
    swaps = []
    for t1, t2 in zip(s1, s2):
        if t1 is not t2:
            swaps.append( (t1, t2) )
            if(len(swaps) > 2): return False

    return swaps[0][0] is swaps[1][1] and swaps[0][1] is swaps[1][0]

print("Meta pairs converse, conserve: {}".format(check_meta_pair('converse', 'conserve')))
print("Meta pairs tags, stag: {}".format(check_meta_pair('tags', 'stag')))

"""
My approach to this puzzle is to use the list of anagrams from previous exercies
because the metathesis pairs are by definitions anagrams of each other.
So, looping through the sets of anagrams and for each combination of two, finding out if
a pair is a metathesis pair
"""


anagrams = anagram_dict("ch9/words.txt") # This file reference, of course, depends on where you're running this script from
print("{} anagrams found".format(len(anagrams)))

metathesis_pairs = []
for key in anagrams:
    anagram_list = anagrams[key]
    for pair in itertools.combinations(anagram_list, 2):
        if check_meta_pair(pair[0], pair[1]): metathesis_pairs.append( (pair[0], pair[1]) )

print("{} metathesis pairs found!".format(len(metathesis_pairs)))
print("Some examples:")

for index, pair in zip(range(100), metathesis_pairs):
    print(pair, end=' ')


