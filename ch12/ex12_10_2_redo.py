"""I originally (partially) solved ex12.10.2 in ex12_10_2.py, however
when I revisited the code to import it as a module for exercise
14.12.2 it was a mess. As a result I'm re-writing it and re-facoring
where necessary here.
"""

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
        l = dict.get(key, [])
        dict[key] = l.append(word)

    return dict

    
