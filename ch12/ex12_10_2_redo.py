"""I originally (partially) solved ex12.10.2 in ex12_10_2.py, however
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
    """

    with open(path) as f:
        for _ in range(skiplines):
            next(f)
        for line in f:
            stripped_line = line.translate(str.maketrans('', '', string.punctuation))
            for word in stripped_line.split():
                yield word


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

def build_anagram_dict(word_gen, starting_dict={}, hash_fn=sorted):
    """This is also based largely on the ex_13_7_7 solution.
    This method returns a reference to the dictionary which was 
    updated or created. 
    """

    dict = starting_dict

    for word in word_gen:
        key = tuple(hash_fn(word))
        word_list = dict.get(key, [])
        dict[key] = word_list + [word]

    return dict

    
