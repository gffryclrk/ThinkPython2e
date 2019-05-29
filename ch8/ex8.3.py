def is_palindrome(string):
    return string == string[::-1]

print('Is dog a palindrome? ', is_palindrome('dog'))
print('Is noon a palindrome? ', is_palindrome('noon'))
print('Is redivider a palindrome? ', is_palindrome('redivider'))
print('Is empty string a palindrome? ', is_palindrome(''))

