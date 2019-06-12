"""
Think Python, 2nd ed
Chapter 10, Exercise 11

Two words are a "reverse pair" if each is the reverse of the other. Write a program that finds all the reverse pairs in the word list. Solution: http://thinkpython2.com/code/reverse_pair.py.

Note: I changed the file naming convention so that I could import the previous exercise for use in the search
"""

# from exercise10_15_11 import in_bisect
# import exercise10_15_11
# import importlib

# importlib.import_module('exercise10_15_10')
import search

pairs = []
words = []
for line in open("../ch9/words.txt"):
    word = line.strip()
    words.append(word)

for word in words:
    if search.in_bisect(words, word[::-1]): pairs.append(word)

print(pairs)

