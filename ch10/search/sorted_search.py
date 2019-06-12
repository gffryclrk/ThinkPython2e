def in_bisect(sorted_list, search, start=0, stop="len", steps=0):
    if stop == "len": stop = len(sorted_list)
    if start >= len(sorted_list) or stop < 0:
        return False

    mid = (start + stop) // 2 

    if sorted_list[mid] == search:
        return True

    if start >= stop:
        return False

    if sorted_list[mid] > search: return in_bisect(sorted_list, search, start, mid - 1, steps+1)
    if sorted_list[mid] < search: return in_bisect(sorted_list, search, mid + 1, stop, steps+1)

