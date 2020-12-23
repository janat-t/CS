from sort_core import swap

#
# BUBBLE SORT
#
# IN:  arbitrary array
# OUT: array with all values sorted in increasing order
#
# METHOD:
#  check online by yourself :)


def sort(array):
    """ Non-destructive bubblesort sort.    
    array is unchanged; returns a sorted copy
    """
    res = array.copy()
    sort_inplace(res)
    return res


def sort_inplace(array):
    """ Inplace bubblesort sort.
    modifies the input array directly
    """
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                swap(array, j, j+1)
    return array

