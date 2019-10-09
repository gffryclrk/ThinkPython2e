"""
Two words are "rotate pairs" if you can rotate one of them and get the other (see rotate_word in Exercise 5).

Write a program that reads a wordlist and finds all the rotate pairs. Solution: http://thinkpython2.com/code/rotate_pairs.py.
"""

from ex8_5 import rot

def rotate_pairs(word_list):
    pairs = []
    for word in word_list:
        for i in range(1,26):
            encoder = rot(i)
            rotated = encoder(word)
            if rotated in word_list:
                pairs.append( (word, rotated, i) )
    return pairs

word_list = {}
for line in open("../ch9/words.txt"):
    word_list[line.rstrip()] = ''

pairs = rotate_pairs(word_list)

print("Found {} pairs!".format(len(pairs)))
print(pairs)
