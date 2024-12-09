#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    """Generates a boolean array indicating prime numbers up to max_n"""
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_n + 1, i):
                primes[multiple] = False

    return primes

def calculate_prime_counts(max_n, primes):
    """Precomputes the number of primes up to each number from 0 to max_n"""
    prime_counts = [0] * (max_n + 1)
    count = 0

    for i in range(max_n + 1):
        if primes[i]:
            count += 1
        prime_counts[i] = count

    return prime_counts

def isWinner(x, nums):
    """Determines the winner of the Prime Game."""
    if not nums or x < 1:
        return None

    max_n = max(nums)

    # Generate primes and precompute counts of primes
    primes = sieve_of_eratosthenes(max_n)
    prime_counts = calculate_prime_counts(max_n, primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
def main():
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

if __name__ == "__main__":
    main()
