# Think Python 2e
## Chapter 11

### Exercise 5

When I first wrote my naive approach to this problem using a list of input words the runtime was approximately 45 minutes (it could have been 1 hour) on this 2017 MBP. I knew this was a bit silly but let it run, and after it finished I changed the list to a dictionary. Using the same code (check the diff!) which is based on Python's `in` keyword, and adding a quick strip() to the input string to remove the newlines, reduced runtime to less than a minute: about 30 seconds. What an unbelievable difference. I expected a performance boost but not that much of one! This reduces the runtime by approximately 99%! Even though this is a toy problem I enjoyed this exercise. 
