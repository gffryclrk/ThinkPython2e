"""
Exercise 1  

Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn't matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

If you did Exercise 10, you can compare the speed of this implementation with the list in operator and the bisection search.
"""

## https://www.peterbe.com/plog/how-to-do-performance-micro-benchmarks-in-python
sys.path.append('../ch10')
# import pandas as pd
# import numpy as np
import search
import random
import time
import statistics

word_dict = {}
word_list = []
for line in open("../ch9/words.txt"):
    word = line.strip()
    word_dict[word] = ''
    word_list.append(word)

print("Size of dictionary: {}".format(len(word_dict)))
print("Size of list: {}".format(len(word_list)))

def f1(word):
    in_bisect(word_list, word)

def f2(word):
    word in word_dict

list_times = []
dict_times = []

for i in range(10000):
    word = random.choice(word_list)

    t0 = time.time()
    search.in_bisect(word_list, word)
    t1 = time.time()
    list_times.append((t1 - t0) * 1000)

    t0 = time.time()
    word in word_dict
    t1 = time.time()
    dict_times.append((t1 - t0) * 1000)

print('in_bisect used {} times with median: {} and mean: {}'.format(len(list_times), statistics.median(list_times), statistics.mean(list_times)))
print('in used {} times with median: {} and mean: {}'.format(len(dict_times), statistics.median(dict_times), statistics.mean(dict_times)))
