"""

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

"""
"""

get_subset

Returns a set of numbers that follows specific rules about the shape of a list of numbers

desc:		up/down/left/right
modifier:	use pos dict below to determine how to get the next index
index:		the index to start on
count:		how many indexes to get

"""
def get_subset(desc, modifier, index, count):
	w = 0
	debug = 0
	subset = list()
	collide = 0
	for i in range(count):
		
		next_index = index+(modifier*i)
		
		## consider edge restrictions ##
		# out of range                
		if next_index < 0 or next_index > w*w:
			if debug: print("next index out of range")
			collide = 1
		# top edge
		if next_index/w < 1 and ("up" in desc):
			if debug: print("hit top edge ", next_index)
			collide = 1
		# left edge
		if next_index%w == 0 and ("left" in desc):
			if debug: print("hit left edge")
			collide = 1
		# right edge
		if (next_index-w-1)%w == 0 and ("right" in desc):
			if debug: print("hit right edge")
			collide = 1
		# bottom edge
		if next_index > (w * w - w) and ("down" in desc):
			if debug: print("hit bottom edge")
			collide = 1
		
		subset.append(next_index)
		if collide is 1:
			return False
		
	if debug: print(index, count, subset)
	return subset	

	
from math import sqrt, floor

def get_width_triangle(grid):
	return int(floor(sqrt(2*len(grid))))

def pad_triangle(w,grid):
	next_element = 0
	print(len(grid))
	padded_grid = [0] * (w*w)
	for i in range(int(w)):
		w-i-1
		padded_grid[i:i-w] = grid[i:i-w]
		print(padded_grid)
		next_element = i+w
	return padded_grid

grid = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4, 82, 47, 65, 19, 1, 23, 75, 3, 34, 88, 2, 77, 73, 7, 63, 67, 99, 65, 4, 28, 6, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

w = get_width_triangle(grid)
padded_grid = pad_triangle(w,grid)


