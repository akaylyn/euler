#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?
import math

def is_prime(x):
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
	
i = 3
primes = [2]
limit = 10001

while True:
	
	if len(primes)==limit:
		break
		
	if is_prime(i):
		primes.append(i)
	
	i+=1

print primes.pop()