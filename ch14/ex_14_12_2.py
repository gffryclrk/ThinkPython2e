""" Think Python, 2nd Ed
Chapter 14, Exercise 2  

If you download my solution to Exercise 2 from
http://thinkpython2.com/code/anagram_sets.py, you’ll see that it
creates a dictionary that maps from a sorted string of letters to the
list of words that can be spelled with those letters. For example,
'opst' maps to the list ['opts', 'post', 'pots', 'spot', 'stop',
'tops'].

Write a module that imports anagram_sets and provides two new
functions: store_anagrams should store the anagram dictionary in a
“shelf”; read_anagrams should look up a word and return a list of its
anagrams. Solution: http://thinkpython2.com/code/anagram_db.py.  """

import sys
sys.path.append('ch12/')
import ex12_10_2_redo as ag

import shelve

def store_anagrams(dict, shelf):
    """This function writes the provided dict to a provided shelf"""
    for k in iter(dict):
        shelf[k] = dict[k]


def read_anagrams(word, shelf):
    """This function reads anagrams from the shelf?
    Pointless if you know how to use the shelve or dbm modules,
    regardless lets provide a wrapper as asked"""

    return shelf[word]

if __name__ == '__main__':
    word_gen = ag.word_gen("text/words.txt")
    dict = ag.build_anagram_dict(word_gen, hash_fn = lambda x: ''.join(sorted(x)))

    db = shelve.open('anagrams')
    store_anagrams(dict, db)
    db.close()

    db = shelve.open('anagrams')
    print(f'returning anagrams for "adeest" from shelf: {", ".join(read_anagrams("adeest", db).keys())}')
    db.close()
