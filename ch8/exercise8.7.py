def counter(string, letter):
    count = 0
    for char in string:
        if letter == char: count += 1
    return count

print('Number of \'l\'s in \'hello\': ', counter('hello', 'l'))
