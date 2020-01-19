"""
More anagrams!

1.  Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of words that are anagrams.

    Here is an example of what the output might look like:

    ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
    ['retainers', 'ternaries']
    ['generating', 'greatening']
    ['resmelts', 'smelters', 'termless']

    Hint: you might want to build a dictionary that maps from a collection of letters to a list of words that can be spelled with those letters. The question is, how can you represent the collection of letters in a way that can be used as a key?

2.  Modify the previous program so that it prints the longest list of anagrams first, followed by the second longest, and so on.
   
3. In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on the board, to form an eight-letter word. What collection of 8 letters forms the most possible bingos?

Solution: http://thinkpython2.com/code/anagram_sets.py.
"""
import pdb

dict = {}
lengths = {}

for line in open("ch9/words.txt"):

    word = line.strip()
    key = tuple(sorted(word))
    word_list = dict.get(key, [])
    word_list.append(word)
    dict[key] = word_list

    length = lengths.get(key, 0)
    length += 1
    lengths[key] = length


print("Found {} anagrams".format(len(dict)))
print("Anagrams for {}: {}".format("deltas", dict[tuple(sorted("deltas"))]))

# 2. Longest Anagrams:
print("Printing top 100 longest anagrams... ")

# This one stumped me for a bit...
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
sorted_anagram_lengths = [key for (key, value) in sorted(lengths.items(), key=lambda item: item[1], reverse=True)]

for index, combo in zip(range(100), sorted_anagram_lengths):
   print("Length {}: {}".format(len(dict[combo]), dict[combo]))

   if len(dict[combo][0]) == 8: print("Combo of length 8: {}".format(combo))

# 3.
# Originally I was going to subset the word list dict..
# However on second thought I decided to simply look at the above loop of ordered letter combo anagram counts for the combo with the most number of anagrams. That combo is ('a', 'e', 'g', 'i', 'n', 'r', 's', 't')

# eight_letter_combos = { k:v for k, v in dict.items() if len(k) == 8 }



