#!/usr/bin/python3
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
def minOperations(n, int):
        return 0
    dp = 0
    i = 2
    while(i <= n):
        if not (n % i):
            n = int(n / i)
            dp += i
            i = 1
            i += 1
            return dp
