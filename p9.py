#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2

#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

a = 3
b = 4
c = 5

limit = 500

# check for a < b < c
def check_size(a, b, c):
	if a < b < c:
		return True
	else:
		return False

# check for a^2 + b^2 = c^2
def is_ptrip(a,b,c):
	a2 = a**2
	b2 = b**2
	c2 = c**2

	if a2 + b2 == c2:
		return True
	else:
		return False

# check for a + b + c = 1000
def check_sum(a,b,c):
	if a+b+c == 1000:
		return True
	else:
		return False

def all_limits(a,b,c):
	if check_size(a,b,c) and is_ptrip(a,b,c):
		return True
	else:
		return False
		
for a in range(limit):
	for b in range(limit):
		c = 1000-a-b
		if all_limits(a, b, c):
			print a, b, c
			print "product: ", a*b*c