"""
As an exercise, use get to write histogram more concisely. You should be able to eliminate the if statement.
"""

def histogram(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1

    return d

print(histogram('brontosaurus'))
