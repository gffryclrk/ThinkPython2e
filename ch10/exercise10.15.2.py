def cumsum(t):
    cumsum = []
    total = 0
    for e in t:
        total += e
        cumsum.append(total)

    return cumsum

t = [1, 2, 3]
print(cumsum(t))
