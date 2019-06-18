"""
Exercise 12  

Two words "interlock" if taking alternating letters from each forms a new word. For example, "shoe" and "cold" interlock to form "schooled". Solution: http://thinkpython2.com/code/interlock.py. Credit: This exercise is inspired by an example at http://puzzlers.org.

    Write a program that finds all pairs of words that interlock. Hint: don't enumerate all pairs!
        Can you find any words that are three-way interlocked; that is, every third letter forms a word, starting from the first, second or third?
"""

import search

words = []
for line in open("../ch9/words.txt"):
    word = line.strip()
    words.append(word)

reverse_pairs = []
for word in words:
    w1 = word[0::2]
    w2 = word[1::2]
    if search.in_bisect(words, w1) and search.in_bisect(words, w2): reverse_pairs.append( (w1, w2, word) )

print(reverse_pairs, "\n", "found {} reverse pairs".format(len(reverse_pairs)))

reverse_pairs_triples = []
for word in words:
    w1 = word[0::3]
    w2 = word[1::3]
    w3 = word[2::3]
    if search.in_bisect(words, w1) and search.in_bisect(words, w2) and search.in_bisect(words, w3): reverse_pairs_triples.append( (w1, w2, w3, word) )

print("\n\n", reverse_pairs_triples, "\n", "found {} reverse pair triples".format(len(reverse_pairs_triples)))
