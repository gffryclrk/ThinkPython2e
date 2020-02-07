## Exercise 6 (skipped)
I skipped exercise 6 because the instruction was to implement the dicitionary differences by using set difference which was the approach I had already taken. 

> Exercise 6
> 
> Python provides a data structure called set that provides many common set operations. You can read about them in Section 19.5, or read the documentation at http://docs.python.org/3/library/stdtypes.html#types-set.
> 
> Write a program that uses set subtraction to find words in the book that are not in the word list. Solution: http://thinkpython2.com/code/analyze_book2.py.

## Exercise 7
I re-implemented bisect search and have been tinkering with the algorithm as I understand it. I managed to implement a version that outputs a word but then began to wonder how one could tell if such an implementation was correct. The challenge is to select words at random, with weighted probabilities, such that the sample (randomly generated) and expected  (actual) word frequency distributions are similar. I want to test the validity of the assumption that the implementation is correct so undertook the task of performing some kind of statistical test.

The statistical test I think is most appropriate for this type of endeavour is chi-square. I found some resources:
- [Chi-Squared Test for Independence in Python](https://codingdisciple.com/chi-squared-python.html)
- [scipy.stats.chisquare](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html)
- [Chi-Squared test in Python (Stack Overflow)](https://stackoverflow.com/questions/9330114/chi-squared-test-in-python)

The implementaton works in the sense that it outputs a random word but even at a glance I'm not convinced of the validitiy. For example, the randomly generated sample distribution contains 158136 (not unique) words: the same as the observed number of words. However, 'the' only occurs once in the randomly generated sample but is #2 in the expected distribution with 5147 occurrences. This seems a large discrepancy.

```{sh}
>>> sample_frenquency_list[0:10]
[10281, 1, 8932, 2, 5949, 0, 2442, 4789, 1, 4481]
>>> sorted_emma_counts_list[0:10]
[('to', 5149), ('the', 5147), ('and', 4613), ('of', 4276), ('a', 3073), ('i', 2968), ('her', 2417), ('it', 2400), ('was', 2376), ('she', 2278)]
>>> sampled_from_distribution['the']
1
>>> sum(sampled_from_distribution.values())
158136
```