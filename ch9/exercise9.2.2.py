def has_no_e(word):
    return word.find('e') < 0

fin = open('words.txt')
no_e = 0
total = 0
for line in fin:
    word = line.strip()
    if has_no_e(word):
        print(word)
        no_e += 1

    total += 1
    
print( no_e / total )

