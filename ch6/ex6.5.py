def gcd(a, b):
	if b == 0: return a
	return gcd(b, a % b)

print('1, 5', gcd(1,5))
print('5, 5', gcd(5,5))
print('25, 5', gcd(25,5))
print('25, 500', gcd(25,500))
print('1929323, 29308230823', gcd(19293232, 293082308232))
