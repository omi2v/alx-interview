#!/usr/bin/python3


""" minimum operation that find single character """
def minOperations(n):
    """
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that calculates
the fewest number of operations needed to result in exactly n
H characters in the file.
More info:
    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
    """
    if not isinstance(n, int):
        return 0
    dp = 0
    p = 2
    while (p <= n):
        if not (n % p):
            n = int(n / 1)
            dp += p
            p = 1
            P += 1
            return dp
