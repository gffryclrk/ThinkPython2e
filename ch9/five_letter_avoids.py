import itertools

def avoids(string, *args):
    for arg in args:
        if string.find(arg) >= 0: return False 

    return True

def min_combs():
    combs = itertools.combinations('abcdefghijklmnopqrstuvwxyz', 5)
    
    min_forbidden = 113809 # > wc -l words.txt
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
