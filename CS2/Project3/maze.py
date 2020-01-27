# -*- coding: utf-8 -*-


import random
import time

# You do *not* need to modify this function
def genRandMaze(n, p):
    """ Generate a random maze of size n x n
    p is the probability that there is a wall between each cell
    Starting point is always the top-left cell (cell 0)
    Goal is always the bottom-right cell (cell n^2-1)

    Cell are numbered from 0 to n^2-1 from top-left to bottom-right
    Output: a graph encoded with adjacency list.
            i.e. a list of n^2 lists of neighbors
    """
    adjList = [ [] for _ in range(n*n)]  # initialize n^2 empty lists
    
    # Generate vertical walls (on the right of cell c)
    for c in range(n*n):
        if c%n == n-1: continue # skip the last column
        if random.random() > p: # There is no wall
            adjList[c].append(c+1) #can move from cell c to c+1
            adjList[c+1].append(c) #can move from cell c+1 to c
    
    # Generate horizontal walls (below the cell c)
    for c in range(n*n - n): # skip the last row
        if random.random() > p: # There is no wall
            adjList[c].append(c+n) #can move from cell c to c+n
            adjList[c+n].append(c) #can move from cell c+n to c
    
    return adjList


# You do *not* need to modify this function
# This function works only for n >= 2
# (anyway, it does not make sense to have a maze of size 1x1...)
def printMaze(n, adjList, visited=None):
    """ Display the maze of size n x n corresponding to adjList
        
        visited is an optional argument:
        a list of Boolean value indicating wether a cell is visited or not
        it will be useful for function BFSMaze below
        
        Note: This function was funny to write.
              Have a look if you are curious :)
              But it is probably not very clear
    """
    # V, H, C are local functions callable only inside this printMaze function
    def V(c): return " " if c+1 in adjList[c] else "│"
    def H(c): return " " if c+n in adjList[c] else "─"
    def C(c): 
        if c == 0: return "S"
        elif visited==None or not visited[c]:
            if c == n**2-1: return "G"
            else: return " "
        else: return "X"
    print("┌"+"───┬"*(n-1)+"───┐")
    print("│ "+C(0)+" "+"".join(V(i)+" "+C(i+1)+" " for i in range(n-1))+"│")
    print("├─"+"─┼─".join(H(i) for i in range(n))+"─┤")
    for r in range(1, n-1):
        print("│ "+C(n*r)+" "+"".join(V(i)+" "+C(i+1)+" " for i in range(n*r, n*r+n-1))+"│")
        print("├─"+ "─┼─".join(H(i) for i in range(n*r,n*r+n))+"─┤")
    print("│"+"".join(" " + C(i)+" "+V(i) for i in range(n**2-n, n**2-1))+" "+C(n**2-1)+" │")
    print("└"+"───┴"*(n-1)+"───┘")


# YOU NEED TO UPDATE THIS FUNCTION
# THERE ARE THREE LINES MISSING
# INDICATED BY XXXXXXX-TODO-XXXXXXX
def BFSMaze(n, adjList, displayDetails=False):
    """ Execute a Breadth First Search algorithm on the maze
        and check if Goal cell is reachable from Start cell
        Return True if the goal is reachable and False if not.
        
        displayDetailsDetails is an optional argument that triggers
        step-by-step printing of the maze. Useful for debugging.
        But then should be set to False to do many simulations.
    """
    if displayDetails:
        print("Initial Maze")
        printMaze(n, adjList)
        time.sleep(1)
    
    # Initialization of the BFS
    visited = [False]*(n**2)  # Keep track of visited cells
    visited[0] = True         # starting cell (cell 0) is visited
    lastVisitedCells = [0]    # initially, only starting cell
    
    # Main loop of the BFS
    step = 0
    while True:
        step += 1                 # Count the number of iterations
        nextVisitedCells = []     # contains the cells that are reachable in one more step
        for c in lastVisitedCells:             # For each cell reached in the previous iteration
            for neigh in adjList[c]:           # look for all its neighbors and check if they have
                if not visited[neigh]:         # have already been visited by the BFS
                    XXXXXXX-TODO-XXXXXXX
                    XXXXXXX-TODO-XXXXXXX
        if nextVisitedCells == []:
            # No new cells visited; it means that BFS is finished
            # All cells connected to the starting cell have been explored
            break  # Exit the loop
        else: # Not yet over, let's update the set (list) of visited cells in the current iteration
            XXXXXXX-TODO-XXXXXXX
            if displayDetails:
                print(f"After {step} iterations, the following cells are reachable:")
                printMaze(n, adjList, visited)
                time.sleep(1)
    
    # From here, the execution of the BFS is over
    # Let's print and return the result (True or False)
    if displayDetails:
        if visited[n**2-1]:    # could also write simpler “visited[-1]”
            print("There is a path from S to G :)")
        else:
            print("There is no path from S to G :(")
    return visited[n**2-1]


if __name__ == "__main__":
    # A simple test to check what BFSMaze is doing
    random.seed(0)
    N = 10
    P = 0.4
    maze = genRandMaze(N, P)
    BFSMaze(N, maze, displayDetails=True)
