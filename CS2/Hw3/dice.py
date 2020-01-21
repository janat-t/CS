import random  # Module needed to generate "random" numbers

random.seed(123)

def one_dice(nb_simulations):
    """ Simulate throwing a 6-sided dice nb_simulations time
    Print the percentage of each possible value (2 to 12).
    """
    counter = [0,0,0,0,0,0,0,0,0,0,0,0]  # shorter version: counter = [0]*12

    for i in range(nb_simulations):
        # Throw a dice and get a random (uniform) result
        x = random.randint(1,6)
        y = random.randint(1,6)
        # Be careful x is in {1,...,12}
        # but lists are indexed from 0
        counter[x+y-1] += 1
    
    print("Raw values:", counter)
    
    for i in range(12):
        # Compute percentage and round with 2 digits after the decimal point
        counter[i] = round( counter[i] * 100 / nb_simulations, 2)    
    
    print("Simulation results:")
    for i in range(2,13):  # i takes values 2,3,...,12
        print(f"The dice value was {i} {counter[i-1]}% of time") # Note the [i-1]

# Run the simulation
one_dice(100000)

