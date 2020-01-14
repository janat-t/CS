from random import sample


def create_random_array(n):
    """ Create an array (list) of n distinct numbers """
    if n < 0: raise ValueError("negative size")
    return sample(range(10*n), k=n)


def swap(array, i, j):
    """ Swap elements at indexes i and j in the array """
    # test validity
    if i >= len(array): raise IndexError(f"index i out of bounds (i={i})")
    if j >= len(array): raise IndexError(f"index j out of bounds (j={j})")
    if i == j: return 
    
    # swap the values
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
    

def is_sorted(array):
    """ Check if the array given as input is sorted """
    for i in range(1,len(array)):
        if array[i-1] > array[i]: return False
    return True
