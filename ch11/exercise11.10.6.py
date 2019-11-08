import pdb
from pronounce import read_dictionary

d = read_dictionary()

print("{} word pronounciations loaded!".format(len(d)))

word_list = {}
for line in open("../ch9/words.txt"):
    word_list[line.rstrip()] = ''

solutions = []
for word in word_list:
    w1 = word[1:]
    w2 = "{}{}".format(word[0], word[2:])
    if w1 in word_list and w2 in word_list and w1 in d and w2 in d and d[w1] == d[w2]: solutions.append(word)

print("{} solutions found: {}".format(len(solutions), solutions))    
