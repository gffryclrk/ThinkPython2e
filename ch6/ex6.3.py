def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

# 1. Type these functions into a file named palindrome.py (whoops!) and test them out.
#    What happens if you call Middle with a string with two letters? Empty string

print('Middle with two letters: ', middle('hi'))

#    One letter? Empty string

print('Middle with one letter: ', middle('h'))

#    What about the empty string, which is written '' and contains no letters? Empty string

print('Middle with empty string: ', middle(''))

# 2. Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise. Remember that you can use the built-in function len to check the length of a string.

def is_palindrome(word):
	# The solution provided will return True for the empty string that I don't like 
	if len(word) < 2: return False
	if len(word) == 2 and word[0] == word[1]: return True
	if len(word) == 3 and word[0] == word[2]: return True
	if word[0] == word[-1]: return is_palindrome(word[1:-1])
	return False

def is_palindrome_solution(word);
	if len(word) <= 1: return True
	if word[0] != word[-1]: return False
	return is_palindrome(word[1:-1])

print('Is dog a palindrome? ', is_palindrome('dog'))
print('Is noon a palindrome? ', is_palindrome('noon'))
print('Is redivider a palindrome? ', is_palindrome('redivider'))
print('Is empty string a palindrome? ', is_palindrome(''))

