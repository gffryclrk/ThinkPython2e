def uses_only(word, letters):
    for c in word:
        if letters.find(c) < 0: return False
    
    return True

print('Cat uses only Ca?: ', uses_only('Cat', 'Ca'))
print('Cat uses only atC?: ', uses_only('Cat', 'atC'))

fin = open('words.txt')
for line in fin:
    word = line.strip()
    if uses_only(word, 'acefhlo'): print(word)
