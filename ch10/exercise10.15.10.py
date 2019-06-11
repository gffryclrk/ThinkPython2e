"""
http://greenteapress.com/thinkpython2/html/thinkpython2011.html#sec128

To check whether a word is in the word list, you could use the in operator, but it would be slow because it searches through the words in order.

Because the words are in alphabetical order, we can speed things up with a bisection search (also known as binary search), which is similar to what you do when you look a word up in the dictionary. You start in the middle and check to see whether the word you are looking for comes before the word in the middle of the list. If so, you search the first half of the list the same way. Otherwise you search the second half.

Either way, you cut the remaining search space in half. If the word list has 113,809 words, it will take about 17 steps to find the word or conclude that it's not there.

Write a function called in_bisect that takes a sorted list and a target value and returns True if the word is in the list and False if it's not.

Or you could read the documentation of the bisect module and use that! Solution: http://thinkpython2.com/code/inlist.py.
"""

import pdb

def in_bisect(sorted_list, search, start=0, stop="len", steps=0):
#   pdb.set_trace()
    if steps == 0: print("Search {} for {}".format(sorted_list[0:10], search))
    if stop == "len": stop = len(sorted_list)
    if start >= len(sorted_list) or stop < 0:
        print("Failed to find {} in {} steps".format(search, steps))
        return False

    mid = (start + stop) // 2 

    if sorted_list[mid] == search:
        print("Found {} in {} steps".format(search, steps))
        return True

    if start >= stop:
        print("Failed to find {} in {} steps".format(search, steps))
        return False

    if sorted_list[mid] > search: return in_bisect(sorted_list, search, start, mid - 1, steps+1)
    if sorted_list[mid] < search: return in_bisect(sorted_list, search, mid + 1, stop, steps+1)

print(in_bisect([1,2,4,5,9,12,14], 2)) 
print(in_bisect([1,2,4,5,9,12,14], 1)) 
print(in_bisect([1,2,4,5,9,12,14], 14)) 
print(in_bisect([1,2,4,5,9,12,14,19,20,22], 14)) 
print(in_bisect([1,2,4,5,9,12,14,19,20,22], 24)) 
print(in_bisect([1,2,5,9,12,14], 2)) 
print(in_bisect([1,2,5,9,12,14], 1)) 
print(in_bisect([1,2,5,9,12,14], 14)) 

sorted_t = []
for line in open('../ch9/words.txt'):
    word = line.strip()
    sorted_t.append(word)

print(in_bisect(sorted_t, "abracadabra"))
print(in_bisect(sorted_t, "notlikelyindictionary"))
