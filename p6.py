#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

limit = 100

sumOfSquares = 0
squareOfSum = 0

for i in range(1,limit+1):
	#print i
	squareOfSum += i
	sumOfSquares += (i**2)


print "sum of squares:",sumOfSquares
print "square of sum:", squareOfSum**2
print abs(sumOfSquares - (squareOfSum**2))