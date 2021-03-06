from sort_core import swap

#
# SELECTION SORT
#
# IN:  arbitrary array
# OUT: array with all values sorted in increasing order
#
# METHOD:
# conceptually, consider two arrays: sorted, unsorted
# initially,
#   sorted   = []
#   unsorted = array
# iteratively,
#   remove the smallest element of unsorted
#   add it at the end of sorted
#

def sort(array):
    """ Non-destructive selection sort.    
    array is unchanged; returns a sorted copy
    """
    res = array.copy()
    sort_inplace(res)
    return res


def sort_inplace(array):
    """ Inplace selection sort.
    modifies the input array directly
    """
    n = len(array)
    for i in range(n-1):
        minidx = i
        for j in range(i, n):
            if array[minidx] > array[j]:
                minidx = j
        swap(array, i, minidx)
    return array

