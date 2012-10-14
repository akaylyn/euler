 
# projecteuler.net problem 4

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(x):
	x_str = str(x)
	if x_str == x_str[::-1]:
		return True
	else:
		return False

num1 = 999
num2 = 999
C = 999

all_palindromes = []
biggest = 0
pair = []
found = False

for i in range(C, 0, -1):
	num1 = i
	for j in range(C, 0, -1):
		num2 = j
		prod = num1*num2
		if is_palindrome(prod):
			all_palindromes.append([num1, num2, prod])
			if prod > biggest:
				biggest = prod
				pair = [num1, num2]

#print all_palindromes
print pair
print biggest