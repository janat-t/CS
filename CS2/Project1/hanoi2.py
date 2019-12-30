# You do NOT need to modify this function
# (except if you want to improve the display)
n = 5
step = 0
block = '#'

def display_tower_hori(pegs):
    for peg in pegs:

        for i in range(n+1, 0, -1):
            print("|", end = "")
            for j in range(n):
                if len(peg) <= j:
                    continue
                if peg[j] >= i: print(block, end = "")
            print()
        print("|", end = "")

        for j in range(n+2):
            print("=", end = "")
        print()

        for i in range(1, n+2):
            print("|", end = "")
            for j in range(n):
                if len(peg) <= j:
                    continue
                if peg[j] >= i: print(block, end = "")
                else: print(" ", end = "")
            print()
        print()


    print()
    print()


def display_tower_vert(pegs):
    for height in range(n + 1, 0, -1):
        for peg in pegs:
            if height <= len(peg):
                num = peg[height-1]
            else:
                num = 0

            for k in range(n - num + 1):
                print(' ', end = '')
            for k in range(num):
                print(block, end = '')
            print('|', end = '')
            for k in range(num):
                print(block, end = '')
            for k in range(n - num + 2):
                print(' ', end = '')
        print()

    for i in range(6 * (n + 2)):
        if (i + 1) % (2 * n + 4) == 0:
            print(' ', end = '')
        else:
            print('=', end = '')

    print()
    print()

def display_tower(pegs):
    display_tower_vert(pegs)
    # display_tower_hori(pegs)

def print_pegs(pegs):
    """Prints the pegs and the disks they contain."""
    for i, peg in enumerate(pegs):
        print(f"{i}: {pegs[i]}")
    print()
    display_tower(pegs)



# You do NOT need to modify this function
# but you can read it to check what it is doing!
def move_disk(pegs, source, dest):
    source %= 3
    dest %= 3
    if pegs[source] == []:       raise AssertionError("source peg is empty")
    disk = pegs[source][-1]
    if pegs[dest] and (pegs[dest][-1] <= disk): raise AssertionError("destination has smaller disk")

    global step
    step += 1
    print(f"STEP {step}: move disk {disk} from peg {source} to peg {dest}")

    pegs[source].pop()     
    pegs[dest].append(disk)

    print_pegs(pegs)


def hanoi(n):
    if n <= 0: raise AssertionError("n must be positive")

    pegs = [[] for _ in range(3)]
    pegs[0] = list(range(n, 0, -1))
    global step
    step = 0
    print("Starting configuration")
    print_pegs(pegs)
    move_tower_clockwise(pegs, n, 0)
    # move_tower_counter_clockwise(pegs, n, 0)
   

##############################################################################
##############################################################################
##############################################################################


def move_tower_clockwise(pegs, nb_disk, source):

    if nb_disk == 1:
        move_disk(pegs, source, source + 1)
    else:
        move_tower_counter_clockwise(pegs, nb_disk - 1, source)
        move_disk(pegs, source, source + 1)
        move_tower_counter_clockwise(pegs, nb_disk - 1, source - 1)

def move_tower_counter_clockwise(pegs, nb_disk, source):

    if nb_disk == 1:
        move_disk(pegs, source, source + 1)
        move_disk(pegs, source + 1, source + 2)
    else:
        move_tower_counter_clockwise(pegs, nb_disk - 1, source)
        move_disk(pegs, source, source + 1)
        move_tower_clockwise(pegs, nb_disk - 1, source - 1)
        move_disk(pegs, source + 1, source + 2)
        move_tower_counter_clockwise(pegs, nb_disk - 1, source)


##############################################################################
##############################################################################

n = int(input("n = "))
hanoi(n)
