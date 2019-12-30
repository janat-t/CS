# Answer to Question 1: O(n) 			Worst case <n> times of equality test
# Answer to Question 2: O(log n)	Worst case <log(base 2) n> times of test

# Input:
# 	elt:		element to search
# 	array:	sorted array (list)
# Output:		index of elt in array or None if elt not in array
def sorted_search(elt, array):
	l, r = 0, len(array)
	while r - l > 1:
		mid = (r + l) // 2
		if elt < array[mid]:
			r = mid
		else:
			l = mid
	if array[l] == elt:
		return l
	return None

a = [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 18, 19]
v = 18
print(sorted_search(v, a))