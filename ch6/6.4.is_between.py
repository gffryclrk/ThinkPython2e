def is_between(x,y,z):
    if x <= y and y <= z: return True
    return False

print('1,2,3 ', is_between(1,2,3))
print('1,5,3 ', is_between(1,5,3))
