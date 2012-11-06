"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from lib import is_prime

limit = 2000000
primesum = 0

for i in range(1, limit+1):
	
	if(is_prime(i)):
		primesum += i

print(primesum)