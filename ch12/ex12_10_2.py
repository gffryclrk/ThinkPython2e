"""
More anagrams!

    Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of words that are anagrams.

    Here is an example of what the output might look like:

    ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
    ['retainers', 'ternaries']
    ['generating', 'greatening']
    ['resmelts', 'smelters', 'termless']

    Hint: you might want to build a dictionary that maps from a collection of letters to a list of words that can be spelled with those letters. The question is, how can you represent the collection of letters in a way that can be used as a key?
"""


dict = {}

for line in open("ch9/words.txt"):
    word = line.strip()
    key = tuple(sorted(word))
    word_list = dict.get(key, [])
    word_list.append(word)
    dict[key] = word_list


print("Found {} anagrams".format(len(dict)))
print("Anagrams for {}: {}".format("deltas", dict[tuple(sorted("deltas"))]))



