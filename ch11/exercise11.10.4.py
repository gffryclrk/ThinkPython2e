"""
If you did Exercise 7 (ch10), you already have a function named has_duplicates that takes a list as a parameter and returns True if there is any object that appears more than once in the list.
"""

def has_duplicates(l):
    dic = {}
    for i in l:
        if i in dic:
            return True
        else:
            dic[i] = 0

    return False

print( "{} has duplicates: {}".format([1,2,3], has_duplicates([1,2,3])) )
print( "{} has duplicates: {}".format([1,2,3,3], has_duplicates([1,2,3,3])) )
print( "{} has duplicates: {}".format([1,2,3,4,5,6,1], has_duplicates([1,2,3,4,5,6,1])) )
print( "{} has duplicates: {}".format([1,9,2,3,4,5,6], has_duplicates([1,9,2,3,4,5,6])) )

