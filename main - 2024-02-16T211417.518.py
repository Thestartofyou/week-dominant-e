def find_weak_dominant_strategy(matrix):
    """
    Find weak dominant strategy for a player in a given payoff matrix.

    Parameters:
    matrix (list of lists): Payoff matrix representing the game.

    Returns:
    int or None: Index of the weak dominant strategy for the player, or None if no weak dominant strategy exists.
    """
    num_strategies = len(matrix)
    for i in range(num_strategies):
        is_weak_dominant = True
        for j in range(num_strategies):
            if matrix[i] < matrix[j] and i != j:  # Check if strategy i is weakly dominated by strategy j
                is_weak_dominant = False
                break
        if is_weak_dominant:
            return i
    return None

# Example usage
player1_payoffs = [[3, 1], [2, 0]]  # Payoff matrix for Player 1
player2_payoffs = [[2, 3], [1, 0]]  # Payoff matrix for Player 2

# Find weak dominant strategies for both players
weak_dominant_strategy_player1 = find_weak_dominant_strategy(player1_payoffs)
weak_dominant_strategy_player2 = find_weak_dominant_strategy(player2_payoffs)

# Print the results
if weak_dominant_strategy_player1 is not None:
    print("Player 1's weak dominant strategy is:", weak_dominant_strategy_player1)
else:
    print("Player 1 has no weak dominant strategy.")

if weak_dominant_strategy_player2 is not None:
    print("Player 2's weak dominant strategy is:", weak_dominant_strategy_player2)
else:
    print("Player 2 has no weak dominant strategy.")
