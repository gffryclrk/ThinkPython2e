def is_anagram(s1, s2):
    a1 = False
    a2 = False
    for c in s1:
        a1 = c in s2

    for c in s2:
        a2 = c in s1

    return a1 and a2

print(is_anagram('dog','god'))
print(is_anagram('dogs','god'))
