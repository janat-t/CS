# You do NOT need to modify this function
# (except if you want to improve the display)
n = 5
step = 0
block = '#'

def display_tower(pegs):
    for height in range(n + 1, 0, -1):
        for peg in pegs:
            if height <= len(peg):
                size = peg[height-1]
            else:
                size = 0

            for k in range(n - size + 1):
                print(' ', end = '')
            for k in range(size):
                print(block, end = '')
            print('|', end = '')
            for k in range(size):
                print(block, end = '')
            for k in range(n - size + 2):
                print(' ', end = '')
        print()

    for i in range(3):
        for j in range(2 * n + 3):
            print('=', end = '')
        print(' ', end = '')

    print()
    print()

def print_pegs(pegs):
    """Prints the pegs and the disks they contain."""
    for i, peg in enumerate(pegs):
        print(f"{i}: {pegs[i]}")
    print()
    display_tower(pegs)



# You do NOT need to modify this function
# but you can read it to check what it is doing!
def move_disk(pegs, source, dest):
    """Moves a single disk from peg source to peg dest.

    Args:
        pegs (array):       Array holding the pegs
        source ({0,1,2}):   Source peg
        dest ({0,1,2}):     Destination peg
    """
    # check if the move is valid
    # If the move is invalid, it will raise an error telling you what is the problem
    if source < 0 or source > 2: raise AssertionError("source index out of bounds")
    if dest < 0 or dest > 2:     raise AssertionError("destination index out of bounds")
    if pegs[source] == []:       raise AssertionError("source peg is empty")
    disk = pegs[source][-1] # disk is the top disk in the source peg
    if pegs[dest] and (pegs[dest][-1] <= disk): raise AssertionError("destination has smaller disk")

    # The move is valid so (i) we print the move on the screen
    global step
    step += 1
    print(f"STEP {step}: move disk {disk} from peg {source} to peg {dest}")

    # then (ii) we execute the move
    pegs[source].pop()       # Take the disk on top of the source peg
    pegs[dest].append(disk)  # and move it to the top of the destination peg

    # and (iii) we display the new configuration
    print_pegs(pegs)


# You do NOT need to modify this function
def hanoi(n):
    """Solves the "Tower of Hanoi" puzzle for n disks."""
    if n <= 0: raise AssertionError("n must be positive")

    # Initialization: the two lines below create the game with 3 pegs
    # and insert n disks on the leftmost peg (peg at index 0)
    # the largest disk is n, then n-1, then ..., until disk 2, and disk 1
    pegs = [[] for _ in range(3)]     # 3 empty pegs
    pegs[0] = list(range(n, 0, -1))   # fill the leftmost peg (peg 0) with n disks
    
    # Display the initial configuration.
    print("Starting configuration")
    print_pegs(pegs)
    
    # move the tower (=the n disks)
    # from the letftmost peg (peg 0) to the central peg (peg 1)
    move_tower(pegs, n, 0, 1)
   

##############################################################################
##############################################################################
##############################################################################


# You HAVE TO modify this function!
# You must write a *recursive* function
# You need to think of two cases:
#    - base case
#    - recursive case
def move_tower(pegs, nb_disk, source, dest):
    """Moves a whole tower of nb_disk disks from source peg to dest peg.
    
    Args:
        pegs (array):        Array holding the pegs
        nb_disk ({1,...,n}): Number of disks to move (i.e. height of the tower)
        source ({0,1,2}):    Source peg (i.e., in which the tower is originally)
        dest ({0,1,2}):      Destination peg (i.e., where to put the tower)
    """
    # spare is the third peg (i.e., neither source nor dest)
    # it may be useful 
    spare = 3 - source - dest

    # TODO: YOU NEED TO WRITE HERE !!!
    # One possible solution can be written as 6 lines below
    # (a different solution is also acceptable)

    if nb_disk == 1:
        move_disk(pegs, source, dest)
    else:
        move_tower(pegs, nb_disk - 1, source, spare)
        move_disk(pegs, source, dest)
        move_tower(pegs, nb_disk - 1, spare, dest)

##############################################################################
##############################################################################

n = int(input("n = "))
hanoi(n)
