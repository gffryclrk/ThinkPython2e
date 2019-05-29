# any_lowercase() returns true if first character of string is lowercase
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

# any_lowercase2) always returns true because 'c'.islower() will always return true (instead of referencing variable c)
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

# This will return whether or not the last character was lowercase (flag is overwritten each iteration of the loop)
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

# This will actually scan the string and return whether or not there are any lowercase letters
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# This will return false upon the first occurence of a non-lowercase letter, even if there are lowercase after
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
