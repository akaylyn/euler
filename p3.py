"""
projecteuler.net - problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import math
num = 600851475143

def is_prime(x):
	foundFactor = 0
	maxPrime = int(math.floor(math.sqrt(x)))
	for i in range(maxPrime):
		if i > 1 and i != x and x % i == 0:
			foundFactor = 1
	if foundFactor == 1:
		return False
	else:
		return True
	
def get_prime_factors(x, primeFactors):
	maxPrime = int(math.floor(math.sqrt(x)))
	prodOfFactors = 1
	for i in range(maxPrime):
		if i > 1 and is_prime(i) and x % i == 0:
			primeFactors.append(i)
			prodOfFactors = 1
			for p in primeFactors:
				prodOfFactors *= p
			
		if prodOfFactors == x:
			return primeFactors
		
		if prodOfFactors > x:
			return False # failed prime factorization
			
	# Didn't find all the prime factors? Find duplicates
	return get_prime_factors(x, primeFactors)

p = []	
print get_prime_factors(num,p)