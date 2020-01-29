"""
From Think Python, 2nd Edition
by Allen B. Downey
http://greenteapress.com/thinkpython2/html/index.html

Exercise 4  

Here’s another Car Talk Puzzler (http://www.cartalk.com/content/puzzlers):

What is the longest English word, that remains a valid English word, as you remove its letters one at a time?

Now, letters can be removed from either end, or the middle, but you can’t rearrange any of the letters. Every time you drop a letter, you wind up with another English word. If you do that, you’re eventually going to wind up with one letter and that too is going to be an English word—one that’s found in the dictionary. I want to know what’s the longest word and how many letters does it have?

I’m going to give you a little modest example: Sprite. Ok? You start off with sprite, you take a letter off, one from the interior of the word, take the r away, and we’re left with the word spite, then we take the e off the end, we’re left with spit, we take the s off, we’re left with pit, it, and I. 

Write a program to find all words that can be reduced in this way, and then find the longest one.

This exercise is a little more challenging than most, so here are some suggestions:

You might want to write a function that takes a word and computes a list of all the words that can be formed by removing one letter. These are the “children” of the word.
Recursively, a word is reducible if any of its children are reducible. As a base case, you can consider the empty string reducible.
The wordlist I provided, words.txt, doesn’t contain single letter words. So you might want to add "I", "a", and the empty string.
To improve the performance of your program, you might want to memoize the words that are known to be reducible.

Solution: http://thinkpython2.com/code/reducible.py.
"""
import itertools
import pdb

word_list = {}
for line in open('ch9/words.txt'):
    word = line.strip()
    word_list[word] = {}

# Add I, a and the empty string
word_list[''] = {}
word_list['I'] = {}
word_list['a'] = {}

def check_word(word, children):
    for i in range(1, len(word)):
        word_less_letter = f'{word[0:i-1]}{word[0+i:len(word)]}'
        if word_less_letter in word_list:
            pdb.set_trace()
            if word_less_letter is not in children: children[word_less_letter] = {}
            check_word(word_less_letter, children)
    

for word in word_list:
    check_word(word, word_list[word])


