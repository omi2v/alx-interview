#!/usr/bin/python3
"""
Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
"""
def sieve_of_eratosthenes(n):
    # Generate all prime numbers up to n
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return primes


def play_game(n, primes):
    if n == 1:
        return False  # Maria loses because there are no prime numbers left to choose

    for prime in primes:
        if prime <= n:
            # Maria picks the largest prime number less than or equal to n
            n -= prime

            if not play_game(n, primes):
                return True  # Maria wins if Ben loses

            n += prime  # Undo Maria's move if Ben wins

    return False  # Maria loses because there are no prime numbers left to choose


def isWinner(x, nums):
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n, primes):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
