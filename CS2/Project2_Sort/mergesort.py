#
# MERGE SORT
#
# IN:  arbitrary array
# OUT: array with all values sorted in increasing order
#
# METHOD:
# recursively,
#   cut the array into two halves: left, right
#   sort each half
#   merge both halves
#

#
# Non-destructive sort:
# array is unchanged
# returns a sorted copy
#


def merge_rec(a, b):
	""" Merge of two sorted arrays (recursive version)
	
	IN:  sorted arrays a and b
	OUT: merging of a and b into one sorted array
	"""
	if not a or not b or a[-1] < b[0]:
		return a + b
	if a[0] < b[0]:
		return [a[0]] + merge_rec(a[1:], b)
	return [b[0]] + merge_rec(a, b[1:])


def merge(a, b):
	""" Merge of two sorted arrays (iterative version)
	
	IN:  sorted arrays a and b
	OUT: merging of a and b into one sorted array
	"""
	res = [0] * (len(a)+len(b))
	indexa = 0
	indexb = 0
	for i in range(len(res)):
		if indexa == len(a): # already used all elements of a
			res[i] = b[indexb]
			indexb += 1
		elif indexb == len(b): # already used all elements of b
			res[i] = a[indexa]
			indexa += 1
		elif a[indexa] < b[indexb]:
			res[i] = a[indexa]
			indexa += 1
		else:
			res[i] = b[indexb]
			indexb += 1
	return res
	
	
def sort(array):
	""" Sorting function (merge sort)
	IN: arbitrary array
	OUT: sorted array
	"""
	##################################
	# TODO *MANDATORY* for project 2 #
	##################################
	# replace the lines below with your own code
	# You can use “merge_rec” or “merge” defined above

	n = len(array)
	if n < 2:
		return array
	mid = n // 2
	left = sort(array[:mid])
	right = sort(array[mid:])
	return merge(left, right)
