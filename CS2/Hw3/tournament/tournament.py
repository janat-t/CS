"""
We would like to organize a tournament between all players.
Tournament is single-elimination bracket with a third place playoff (for the losers of semi-finals).
After the tournament, there are four players ranked 1st, 2nd, 3rd, and 4th.

Initial position in the bracket is (uniformly) random.
We want to to estimate the chance of each player to finish in a good position (1 to 4)
"""

import random

# Global variables
# Remark: Not a very good practice to use global variables,
#         but it is OK for short/quick program like today!
NB_PLAYERS = 32
STRENGTH = [79, 79, 22, 85, 98, 59, 56, 60, 47, 53, 69, 20, 79, 11, 58, 30, 26, 52, 85, 26, 77, 19, 60, 57, 13, 90, 85, 20, 62, 79, 68, 95]


def compute_winner(player1, player2):
    """ Compute the winner between two players.
    
    This function is non-deterministic.
    """
    s1 = STRENGTH[player1]
    s2 = STRENGTH[player2]
    if random.random() < s1 / (s1 + s2):
        return player1
    else:
        return player2


def simulate_tournament():
    """ Simulate a tournament with all NB_PLAYERS players
    
    1) Generate a random bracket
    2) Simulate the competition
    3) Return the identities of the players ranked 1 to 4
    
    Note 1: This function works only when NB_PLAYERS is a power of 2.
    Note 2: This function does not take arguments.
            It will consider NB_PLAYERS players with their strength given in the global variable STRENGTH.
    """
    players = list(range(NB_PLAYERS))  # List containing all players = [0,1,...,31]
    random.shuffle(players)            # Shuffle to generate random bracket

    nb_players = NB_PLAYERS  # Number of players not yet eliminated
    
    # This loop simulates all games of a given round until semi-final (excluded)
    while nb_players > 4: # Not yet semi-final
        next_round_players = []         # List that will contain all winners of this round, i.e. players of the next round
        for k in range(nb_players//2):  # Given N players at the begining of the round,
            p1 = players[2*k]           # there are N//2 games to be played
            p2 = players[2*k+1]         # players[0]-vs-players[1], players[2]-vs-players[3], ...
            win_p1_vs_p2 = compute_winner(p1, p2)
            next_round_players.append(win_p1_vs_p2)
        players = next_round_players
        nb_players = nb_players//2     # Half of players have been eliminated
    
    # Now there are only 4 players
    # first semi-final
    p1 = players[0]
    p2 = players[1]
    win_first_semi = compute_winner(p1, p2)
    loose_first_semi = p1 + p2 - win_first_semi     # A "nice" hack to obtain the loser player
    
    # second semi-final
    p1 = players[2]
    p2 = players[3]
    win_second_semi = compute_winner(p1, p2)
    loose_second_semi = p1 + p2 - win_second_semi
    
    # final
    rank_1 = compute_winner(win_first_semi, win_second_semi)
    rank_2 = win_first_semi + win_second_semi - rank_1
    
    # third-place game
    rank_3 = compute_winner(loose_first_semi, loose_second_semi)
    rank_4 = loose_first_semi + loose_second_semi - rank_3
    
    # Return the result of the simulation
    return (rank_1, rank_2, rank_3, rank_4)   # parenthesis are optional here



def compute_stats(nb_simu):
    """ Compute statistics based on nb_simu tournaments 
    
    Let's give the following points to the top players:
        - 100 points to the winner
        - 60  points to the runner-up
        - 30  points for 3rd position
        - 10  point  for 4th position
    """
    average_point_per_player = [0]*NB_PLAYERS
    
    for _ in range(nb_simu):
        result = simulate_tournament()       # result is a tuple of four players
        rank1, rank2, rank3, rank4 = result
        average_point_per_player[rank1] += 100
        average_point_per_player[rank2] += 60
        average_point_per_player[rank3] += 30
        average_point_per_player[rank4] += 10
    
    average_point_per_player = [round(x/nb_simu,2) for x in average_point_per_player] # Again, list comprehension here
    
    # data is a *bad* name. But I did not find a good name yet...
    # Create a list of pair. Each pair contains two elements:
    #     - the average points of a player
    #     - the identity of the player
    # Note that the order of elements (in the pair) is important for sorting
    data = [(average_point_per_player[i], i) for i in range(NB_PLAYERS)]
    data.sort(reverse=True)  # Sort reverse to put player with more points first
    for pair in data:
        print(f"Player {pair[1]} with strength {STRENGTH[pair[1]]} got {pair[0]} points in average")

if __name__ == '__main__':
    compute_stats(1000)


