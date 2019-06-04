import pdb 

def in_bisect(sorted_list, search, start=0, stop=-1, steps=0):
    if stop < 0: stop = len(sorted_list) - 1
    if stop > len(sorted_list) or start < 0: return False
    # pdb.set_trace()

    # mid = len(sorted_list) // 2
    mid = start + ((stop - start) // 2)
    print("Searching for ", search, " step ", steps, " mid: ", mid)
    if sorted_list[mid] == search: return True
    if sorted_list[mid] > search: return in_bisect(sorted_list, search, start, mid - 1, steps+1)
    else: return in_bisect(sorted_list, search, mid+1, mid + (stop - start), steps+1)


print(in_bisect([1,2,4,5,9,12,14], 2)) 
print(in_bisect([1,2,4,5,9,12,14], 1)) 
print(in_bisect([1,2,4,5,9,12,14], 14)) 
print(in_bisect([1,2,4,5,9,12,14,19,20,22], 14)) 
print(in_bisect([1,2,4,5,9,12,14,19,20,22], 24)) 
# print(in_bisect([1,2,5,9,12,14], 2)) 
# print(in_bisect([1,2,5,9,12,14], 1)) 
# print(in_bisect([1,2,5,9,12,14], 14)) 
