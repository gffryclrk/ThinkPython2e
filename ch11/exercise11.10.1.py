"""
Exercise 1  

Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn't matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

If you did Exercise 10, you can compare the speed of this implementation with the list in operator and the bisection search.
"""
import pandas as pd

word_dict = {}
word_list = []
for line in open("../ch9/words.txt"):
    word = line.strip()
    word_dict[word] = ''
    word_list.append(word)

print("Size of dictionary: {}".format(len(word_dict)))
print("Size of list: {}".format(len(word_list)))


