def uses_all(word, letters):
    for c in letters:
        if word.find(c) < 0: return False
    
    return True


print('cat uses all \'ca\'? ', uses_all('cat', 'ca'))
print('cat uses all \'caz\'? ', uses_all('cat', 'caz'))

fin = open('words.txt')
counter = 0
for line in fin:
    word = line.strip()
    if uses_all(word, 'aeiou'):
        print(word)
        counter += 1

print(counter)
fin.close()

fin = open('words.txt')
counter = 0
for line in fin:
    word = line.strip()
    if uses_all(word, 'aeiouy'):
        print(word)
        counter += 1

print(counter)
fin.close()
