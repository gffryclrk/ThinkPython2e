import itertools
import pdb

def avoids(string, *args):
    for arg in args:
        if string.find(arg) >= 0: return False 

    return True

print("Cat avoids a?: ", avoids('Cat', 'a'))
print("Cat avoids z?: ", avoids('Cat', 'z'))
print("Cat avoids z, x?: ", avoids('Cat', 'z', 'x'))
print("Cat avoids Ca?: ", avoids('Cat', 'Ca'))
print("Cat avoids Ba?: ", avoids('Cat', 'Ba'))
print("Cat avoids Ca, Ba?: ", avoids('Cat', 'Ca', 'Ba'))

print('Please input string of forbidden letters')
forbidden = input('> ')
char_forbidden = list(forbidden)

fin = open('words.txt')

total = 0
no_forbidden = 0
for line in fin:
    word = line.strip()
    if avoids(word, *char_forbidden): no_forbidden += 1
    total += 1

fin.close()

print('Total number of words that avoid your letters: {} '.format(no_forbidden))

combs = itertools.combinations('abcdefghijklmnopqrstuvwxyz', 5)

min_forbidden = total
# min_forbidden_letters = ''

for comb in combs:
    # pdb.set_trace()

    fin = open('words.txt')
    no_forbidden = 0
    for line in fin:
        word = line.strip()
        if avoids(word, *comb): no_forbidden += 1
    fin.close()

    if no_forbidden < min_forbidden:
        min_forbidden = no_forbidden
        min_forbidden_letters = comb
        print(min_forbidden, min_forbidden_letters)

print(comb, ' produces the minimum number of letters, {}'.format(min_forbidden))
