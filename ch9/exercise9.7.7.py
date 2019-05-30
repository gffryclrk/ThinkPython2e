import pdb

def three_consecutive(word):
    # pdb.set_trace()
    if(len(word) < 6): return False

    doubles = []
    for i in range(0, len(word) - 1):
        if word[i] == word[i+1]: doubles.append(i)
 
    if len(doubles) < 3: return False
    found_three = False
    for i in range(0, len(doubles)-2):
#         if doubles[i] + 2 != doubles[i+1]: return False
        if doubles[i] + 4 == doubles[i+1] + 2 == doubles[i+2]: found_three = True

    return found_three

print('Three consecutive: aabbcc ', three_consecutive('aabbcc'))
print('Three consecutive: aabbzcc', three_consecutive('aabbzcc'))
print('Three consecutive: aaoaabbcc ', three_consecutive('aaoaabbcc'))
print('Three consecutive: mississippi ', three_consecutive('mississippi'))
print('Three consecutive: aazz ', three_consecutive('aazz'))

fin = open('words.txt')
for line in fin:
    word = line.strip()
    if three_consecutive(word): print(word)

fin.close()

