"""
I use this file to generate 32 players
Then we will use the data to simulate
tournaments between these players
"""

import random
random.seed(2020)

# Number of players
NB_PLAYERS = 32

# Array (list) to store the strength of each player
players_strength = []

# Generate random strength for each player
for _ in range(NB_PLAYERS):     # _ can be used when the index is not used
    s = random.randint(0, 100)
    players_strength.append(s)

print(players_strength)

# players_strength = [79, 79, 22, 85, 98, 59, 56, 60, 47, 53, 69, 20, 79, 11, 58, 30, 26, 52, 85, 26, 77, 19, 60, 57, 13, 90, 85, 20, 62, 79, 68, 95]