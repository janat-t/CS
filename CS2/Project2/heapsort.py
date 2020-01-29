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

def shiftdown(idx, heap):
	swap = idx
	if R(idx) < len(heap):
		if heap[idx] > min(heap[L(idx)], heap[R(idx)]):
			swap = L(idx) if heap[L(idx)]<heap[R(idx)] else R(idx)
	elif L(idx) < len(heap):
		if heap[idx] > heap[L(idx)]:
			swap = L(idx)
	if swap == idx:
		return
	tmp = heap[idx]
	heap[idx] = heap[swap]
	heap[swap] = tmp
	shiftdown(swap, heap)

def pop(heap):
	n = len(heap)
	tmp = heap[0]
	heap[0] = heap[n-1]
	heap.pop()
	shiftdown(0, heap)
	return tmp

def heapify(array):
	heap = array.copy()
	n = len(array)
	for i in range(n-1, -1, -1):
		shiftdown(i, heap)
	return heap


def sort(array):
	""" Sorting function (merge sort)
	IN: arbitrary array
	OUT: sorted array
	"""
	n = len(array)
	heap = heapify(array)
	res = [pop(heap) for i in range(n)]
	return res