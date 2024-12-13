#!/usr/bin/python3

def is_prime(n):
    """Efficiently checks if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    """Generates a list of primes up to n using the Sieve of Eratosthenes."""
    primes = []
    is_prime_list = [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime_list[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime_list[j] = False
    return primes

def isWinner(x, nums):
    """Determines the winner of the Prime Game."""
    if not nums or x <= 0:
        return None

    max_n = max(nums) if nums else 0
    primes = get_primes(max_n)
    prime_counts = [0] * (max_n + 1)

    for i in range(1, max_n + 1):
        count = 0
        for p in primes:
            if p > i:
                break
            if i % p == 0:
                count += 1
        prime_counts[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 0 or n == 1:
            ben_wins += 1
            continue
        if prime_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
            
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
