def find(word, letter, start=0):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print('Index of \'l\' in \'hello\': ', find('hello', 'l', 1))
