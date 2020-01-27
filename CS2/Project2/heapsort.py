#
# MERGE SORT
#
# IN:  arbitrary array
# OUT: array with all values sorted in increasing order
#
# METHOD:
# Make the array into minheap [O(n)],
# 	then select the top of the heap
# 	into a new sorted array [O(nlogn)]
#   Total O(nlogn)
#

def L(idx):
	return 2*idx+1

def R(idx):
	return 2*idx+2

def shiftdown(idx, array):
	swap = idx
	if R(idx) < len(array):
		if array[idx] > min(array[L(idx)], array[R(idx)]):
			swap = L(idx) if array[L(idx)]<array[R(idx)] else R(idx)


		


def heapify(array):
	heap = array.copy()
	for i in range(n-1, 0, -1):
		shiftdown(i, array)

def sort(array):
	""" Sorting function (merge sort)
	IN: arbitrary array
	OUT: sorted array
	"""
	n = len(array)
	heap = heapify(array)
	res = [0]*n
	for i in range(n):
		shiftdown(i, array)
