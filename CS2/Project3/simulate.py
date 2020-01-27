# -*- coding: utf-8 -*-


from maze import genRandMaze, BFSMaze # To access functions defined in the other file
import matplotlib.pyplot as plt       # To plot graphics directly in python

# YOU HAVE TO WRITE THIS FUNCTION
def simulateFixedParameters(n, p, nbSimus):
    """ Execute *nbSimus* simulations:
        - Generate a maze with parameters *n* and *p*
        - Check if there is a path from S to G
        Return the percentage of success (success=there is path from S to G)
    """
    ########################
    ######### TODO #########
    ########################

    return 0   # Of course you need to remove this “return 0”


# You do *not* need to modify this function
# But you can if you want to change something
def simulate(n, listP, nbSimus):
    """ Excecute nbSimus simulations for all values of p in listP
        Return the list of percentage of success for each value of p
    """
    results = []
    for p in listP:
        results.append( simulateFixedParameters(n, p, nbSimus) )
    return results



if __name__ == "__main__":
    # simulate function gives us data that we can use
    # to plot some nice curves
    
    # You can/should modify the values below
    listP = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    data10 = simulate(10, listP, 5)
    
    # Example of curve that you can obtain
    # Note: axis labels, title, ... are missing
    #       they should be added to have proper graphic
    plt.plot(listP, data10)
