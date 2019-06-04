# I just ran the above script and received the following output:
# V1:  0.104835186  V2:  85.661089808  V1 < V2:  True
# v1 is faster because it doesn't recreate a new list everytime so there's less overhead
# v2 re-creates a new list with one extra item 110,000 or so times (# of lines in the file) and then assigns that list to the variable. This results in v1 being about 856 times faster.

import timeit

def words_list_v1(f):
    fin = open(f)
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)

    fin.close()
    return t

def words_list_v2(f):
    fin = open(f)
    t = []
    for line in fin:
        word = line.strip()
        t = t + [line]

    fin.close()
    return t

f = '..\ch9\words.txt'

start = timeit.default_timer()
words_list_v1(f)
stop = timeit.default_timer()

v1_time = stop - start

start = timeit.default_timer()
words_list_v2(f)
stop = timeit.default_timer()

v2_time = stop - start

print("V1: ", v1_time, " V2: ", v2_time, " V1 < V2: ", v1_time < v2_time)

