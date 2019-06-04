import pdb

def nested_total(t, total=0):
#    pdb.set_trace()
    for e in t:
        if type(e) == list: total += nested_total(e)
        else: total += e

    return total

ttl = nested_total([1, [1, 2], [3, 4]])
print(ttl)
ttl = nested_total([1, [1, 2], [3, 4], [1, [1, [3, 4]]]])
print(ttl)

