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


# 2018 version
# ==> replaced with function below which is more clear (hoepefully)
#def merge(a, b):
#    """ Merge of two sorted arrays (iterative version)
#    
#    IN:  sorted arrays a and b
#    OUT: merging of a and b into one sorted array
#    """
#    if not a or not b or a[-1] < b[0]:
#        return a + b
#    res = [ a[0] for i in range(len(a)+len(b)) ]
#    next_a = 0
#    last_a = len(a)-1
#    last_b = len(b)-1
#    for i in range(len(res)):
#        next_b = i - next_a
#        if (next_a > last_a) or ((next_b <= last_b) and (a[next_a] > b[next_b])):
#            res[i] = b[next_b]
#        else:
#            res[i] = a[next_a]
#            next_a += 1
#    return res


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

def myMerge(a, b):
	i = 0
	j = 0
	idx = 0
	m = len(a)
	n = len(b)
	res = [0] * (m + n)
	while i < m and j < n:
		if a[i] < b[j]:
			res[idx] = a[i]
			i += 1
		else:
			res[idx] = b[j]
			j += 1
		idx += 1
	while i < m:
		res[idx] = a[i]
		idx += 1
		i += 1
	while j < n:
		res[idx] = b[j]
		idx += 1
		j += 1
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
	return myMerge(left, right)