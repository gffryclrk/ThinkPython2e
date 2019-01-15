def is_triangle(s1, s2, s3):
    if s1 > (s2 + s3) or s2 > (s1 + s3) or s3 > (s2 + s3): print("No")
    elif s1 == (s2 + s3) or s2 == (s1 + s3) or s3 == (s2 + s3): print("Degenerate")
    else: print("yes")

print("1, 2, 3?")
is_triangle(1,2,3)
print("\n4, 5, 6?")
is_triangle(4,5,6)
print("\n10, 2, 1?")
is_triangle(10,2,1)
print("\n4, 2, 2?")
is_triangle(4,2,2)
