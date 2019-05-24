def is_power(a, b):
	if a == b: return True
	if a % b == 0: return is_power(a/b, b)
	return False

print('8, 2', is_power(8,2))
print('9, 2', is_power(9,2))
print('16, 2', is_power(16,2))
print('3, 2', is_power(3,2))
print('169, 3', is_power(169,3))
print('1024, 2', is_power(1024,2))
