"""
http://greenteapress.com/thinkpython2/html/thinkpython2013.html
Exercise 1  

Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at http://en.wikipedia.org/wiki/Letter_frequencies. Solution: http://thinkpython2.com/code/most_frequent.py. 
"""
def most_frequent(s):
    dict = {}
    for letter in s:
        dict[letter] = dict.get(letter, 0) + 1
        
    freqs = [ (key, value) for (key, value) in sorted(dict.items(), key=lambda x: x[1], reverse=True) ]

    # Instruction was to print order but I'm going to just return the sorted list of tuples
    # in classic word count fashion :)
    
    return freqs


print("most frequent hello: {}".format(most_frequent('hello')))
print("most frequent abracadbra: {}".format(most_frequent('abracadbra')))
