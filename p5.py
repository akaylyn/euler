# project euler problem 5

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

i = 232790000
#i = 1
r = 20
while True:
	print i
	flag = False
	c = 1
	for j in range(1,r+1):
		if(i%j == 0):
			c+=1
		else:
			break
		if(c == r+1):
			flag = True
	
	if flag:
		print "result: ", i
		break
	i+=1