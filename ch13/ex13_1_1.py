"""
From Think Python, 2nd Ed.
http://greenteapress.com/thinkpython2/html/thinkpython2014.html

Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.

Hint: The string module provides a string named whitespace, which contains space, tab, newline, etc., and punctuation which contains the punctuation characters. Let’s see if we can make Python swear:

>>> import string
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

Also, you might consider using the string methods strip, replace and translate. 
"""
import string

def read_file(filename, skiplines=0):
    """
    This function reads from a file, line by line, strips whitespace and punctuation, and outputs words one at a time
    """

    punct_trans_table = str.maketrans(dict.fromkeys(string.punctuation))
    whitespace_trans_table = str.maketrans(dict.fromkeys(string.whitespace))
    
    def word_generator():
        """
        Creates a generator from filename provided to outer function. Skips specified numebr of lines.
        """
        
        with open(filename) as f:
            for _ in range(skiplines):
                next(f)
            for line in f:
                for word in line.translate(punct_trans_table).split():
                    yield word.translate(whitespace_trans_table)

    return word_generator()

if __name__ == "__main__":
    word_gen = read_file('text/sherlock_1661-0.txt')
    for a in range(1, 12):
        print("Word {}: {}".format(a, next(word_gen)))
    
            
