# -*- coding: utf-8 -*-


from maze import genRandMaze, BFSMaze # To access functions defined in the other file
from tqdm import tqdm                 # To create a beautiful progress bar
import matplotlib.pyplot as plt       # To plot graphics directly in python
import numpy as np

# YOU HAVE TO WRITE THIS FUNCTION
def simulateFixedParameters(N, P, nbSimus):
    """ Execute *nbSimus* simulations:
        - Generate a maze with parameters *n* and *p*
        - Check if there is a path from S to G
        Return the percentage of success (success=there is path from S to G)
    """
    success_count = 0
    for i in range(nbSimus):
        maze = genRandMaze(N, P)
        if BFSMaze(N, maze):
            success_count += 1

    return success_count / nbSimus * 100   # Return th rate of success


# You do *not* need to modify this function
# But you can if you want to change something
def simulate(N, listP, nbSimus):
    """ Excecute nbSimus simulations for all values of P in listP
        Return the list of percentage of success for each value of P
    """
    results = []
    for P in tqdm(listP):
        results.append( simulateFixedParameters(N, P, nbSimus) )
    return results



if __name__ == "__main__":
    # simulate function gives us data that we can use
    # to plot some nice curves
    
    # You can/should modify the values below
    finest = 4              # Finest of the graph (1, 2, 3, ...)
    nbSimus = 10000         # Number of Simulations
    N = 10                  # Size of the maze

    listP = np.linspace(0.0, 1.0, finest * 10 + 1)
    data = simulate(N, listP, nbSimus)
    
    # Example of curve that you can obtain
    # Note: axis labels, title, ... are missing
    #       they should be added to have proper graphic
    plt.plot(listP, data)
    plt.show()
