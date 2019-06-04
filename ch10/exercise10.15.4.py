def chop(t):
    if len(t) < 3: return
    del t[0]
    del t[len(t) -1]

t = [1,2,3,4]
chop(t)
print(t)
