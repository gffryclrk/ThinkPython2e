def has_duplicates(t):
    if len(t) > len(set(t)): return True
    return False

print(has_duplicates([1,2,2,3]))
print(has_duplicates([1,2,3]))

