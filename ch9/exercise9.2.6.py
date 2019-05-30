def is_abecedarian(word):
    word = word.lower()
    first = ord(word[0])
    for c in word[1:]:
        this = ord(c)
        if this < first: return False
        first = ord(c)
    return True

print('abcde: ', is_abecedarian('abcde'))
print('zebra: ', is_abecedarian('zebra'))
