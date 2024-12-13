#!/usr/bin/python3

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_winner(n):
    """Determine the winner for a single game up to n."""
    if n < 1:
        return 0

    nums = list(range(1, n + 1))
    maria_turn = True
    moves = 0

    while True:
        possible_moves = []
        for num in nums:
            if is_prime(num):
                possible_moves.append(num)

        if not possible_moves:
            break

        chosen_prime = possible_moves[0]  # Optimal play: choose the 
        nums = [num for num in nums if num % chosen_prime != 0]
        moves += 1
        maria_turn = not maria_turn

    if moves % 2 == 1:  # Odd number of moves means Maria won
        return 1
    else:
        return 0

def isWinner(x, nums):
    """Determine the overall winner across multiple games."""
    if not nums or x <= 0:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = get_winner(n)
        if winner == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
