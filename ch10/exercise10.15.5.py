def is_sorted(t):
    i = 0
    while i < len(t) - 1:
        if t[i] > t[i + 1]: return False 
        i += 1

    return True

print(is_sorted([1,2,3]))
print(is_sorted(['b','a']))
        
