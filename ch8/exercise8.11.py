# is_reverse('pots', 'stop')
#   word1 -> 'pots'
#   word2 -> 'stop'
#   i -> 0
#   j -> 3
#
#   j > 0 -> True
#   word1[i] -> p
#   word2[j] -> p
#   p == p -> True
#   i -> 1
#   j -> 2
#
#   j > 0 -> True
#   word1[i] -> o
#   word2[j] -> o
#   o == o -> True
#   i -> 2
#   j -> 1
#
#   j > 0 -> True
#   word1[i] -> t
#   word2[j] -> t
#   t == t -> True
#   i -> 3
#   j -> 0
#
#   j > 0 -> False
#

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1

    while j >= 0:
        print(i, j)

        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1

    return True

print(is_reverse('pots','stop'))
