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
    # TODO (OPTIONAL): implement bubblesort sort
    # replace the lines below with your own code
    list.sort(array)
    return array

