#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of the prime game over x rounds.
    Maria and Ben take turns removing prime numbers and their multiples.
    Returns:
        "Maria" if Maria wins more rounds,
        "Ben" if Ben wins more rounds,
        None if the result is a tie.
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)

    # Sieve of Eratosthenes to identify primes up to max_n
    is_prime = [True for _ in range(max_n + 1)]
    is_prime[0] = False
    if max_n >= 1:
        is_prime[1] = False

    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    # Precompute the prefix sums of prime counts
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round
    for n in nums:
        # If count of primes up to n is odd, Maria wins, else Ben wins
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
