"""
Memoize the Ackermann function from Exercise 2 and see if memoization makes it possible to evaluate the function with bigger arguments. Hint: no
"""
memo = {}

def ack(m, n):
    if (m, n) in memo:
        return memo[(m, n)]    

    if m is 0:
        res = n + 1
    if m > 0 and n == 0:
        res = ack(m - 1, 1)
    if m > 0 and n > 0:
        res = ack(m -1, ack(m, n - 1)) 

    memo[(m,n)] = res
    return res

print("(m,n) = (3,4): {}".format(ack(3,4)))
# print("(m,n) = (10,4): {}".format(ack(10,4)))
# print("(m,n) = (5,4): {}".format(ack(5,4)))
# print("(m,n) = (15,4): {}".format(ack(15,4)))


