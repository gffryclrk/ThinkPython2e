def cumsum(t):
    cumsum = []
    total = 0
    for e in t:
        total += e
        cumsum.append(total)

    return cumsum


if __name__ == '__main__':
    t = [1, 2, 3]
    print(cumsum(t))
