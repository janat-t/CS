import random  # Module needed to generate "random" numbers
from matplotlib import pyplot as plt

random.seed(123)

def n_dice(nb_dice, nb_simulations):
    counter = [0]*(6 * nb_dice)

    for i in range(nb_simulations):
        # Throw a dice and get a random (uniform) result
        sum = 0
        for i in range(nb_dice):
            sum += random.randint(1,6)
        # Be careful x is in {1,...,12}
        # but lists are indexed from 0
        counter[sum-1] += 1
    
    print("Raw values:", counter)
    
    for i in range(6 * nb_dice):
        # Compute percentage and round with 2 digits after the decimal point
        counter[i] = round( counter[i] * 100 / nb_simulations, 2)    
    
    print("Simulation results:")
    for i in range(6 * nb_dice):  # i takes values 2,3,...,12
        print(f"The dice value was {i+1} {counter[i]}% of time") # Note the [i-1]
    return counter

# Run the simulation

D = 6
N = 100000
for D in range(2,9):
    x = [i+1 for i in range(6 * D)]
    data = n_dice(D, N)
    plt.bar(x, data)
plt.show()
