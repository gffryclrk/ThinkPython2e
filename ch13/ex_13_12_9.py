"""
Think Python, 2nd Ed.
http://greenteapress.com/thinkpython2/html/thinkpython2014.html

Chapter 13
Section 12
Exercise 9  

The “rank” of a word is its position in a list of words sorted by frequency: the most common word has rank 1, the second most common has rank 2, etc.

Zipf’s law describes a relationship between the ranks and frequencies of words in natural languages (http://en.wikipedia.org/wiki/Zipf's_law). Specifically, it predicts that the frequency, f, of the word with rank r is:
f = c r−s 

where s and c are parameters that depend on the language and the text. If you take the logarithm of both sides of this equation, you get:
logf = logc − s logr 

So if you plot log f versus log r, you should get a straight line with slope −s and intercept log c.

Write a program that reads a text from a file, counts word frequencies, and prints one line for each word, in descending order of frequency, with log f and log r. Use the graphing program of your choice to plot the results and check whether they form a straight line. Can you estimate the value of s?
"""
import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

import pdb

def build_freq_dict(path):
    """
    This function takes a path and builds a dictionary
    of (k,v) = (word, frequency)
    """

    freq_dict = {}
    with open(path, 'r') as f:
        for line in f:
            for word in line.strip().split():
                count = freq_dict.get(word, 0) + 1
                freq_dict[word] = count

    return freq_dict

if __name__ == '__main__':
    emma_frequencies = build_freq_dict('text/emma.txt')
    print(f"Emma Frequencies Dictionary length: {len(emma_frequencies)}")

    sorted_emma_frequencies = [(k,v) for (k,v) in sorted(emma_frequencies.items(), key=lambda x: x[1], reverse=True)]

    # print(sorted_emma_frequencies[0:10])  

    print("Top ten highest frequencies:")
    for i, (k,v) in enumerate(sorted_emma_frequencies[0:10]):
        """
        Log 0 is undefined, hence i + 1
        """
        
        # pdb.set_trace()
        print(f"t: ({k}, {v}), r: {i+1}, log r: {math.log(i + 1)}, log f: {math.log(v)}")

    logf_list = [math.log(x[1]) for ind, x in enumerate(sorted_emma_frequencies)]

    logr_list = [math.log(ind+1) for ind in range(0, len(sorted_emma_frequencies))]

    assert(len(logf_list) == len(logr_list))

    """
    Use the graphing program of your choice to plot the results and check whether they form a straight line.
    
    Line is relatively straight with a negative slope
    """
    plt.scatter(logr_list, logf_list, s=5)
   
    
    """
    Can you estimate the value of s?
    This seems like a job for regression!
    """


    logr_array = np.array(logr_list).reshape((-1, 1))
    logf_array = np.array(logf_list)
    model = LinearRegression().fit(logr_array, logf_array)

    print(f"Model coefficient of determination: {model.score(logr_array, logf_array)}")
    print("f = c * r^(-s) ")
    print(f"intercept (c): {model.intercept_}")
    print(f"slope (s): {model.coef_}")

    plt.show()

    


