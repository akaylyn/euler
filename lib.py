import math

def is_prime(x):

	if x == 0 or x == 1:
		return False

	if x == 2:
		return True

	if is_even(x):
		return False
	maxPrime = int(math.floor(math.sqrt(x)))

	for i in range(3, maxPrime+1, 2):
		if x % i == 0:
			return False
	return True

def is_even(x):
	if x % 2 == 0:
		return True
	return False 