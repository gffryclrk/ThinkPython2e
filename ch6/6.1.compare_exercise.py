def compare(x, y):
    if x > y: return 1
    if x == y: return 0
    if x < y: return -1

print("1, 2", compare(1, 2))
print("2, 2", compare(2, 2))
print("2, 1", compare(2, 1))


