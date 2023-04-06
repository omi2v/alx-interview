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
    con = 1
    p_list = []
    val = num
    while val != 1:
        con += 1
        if val % con == 0:
            while (val % con == 0 and val != 1):
                val /= con
                p_list.append(con)

    return p_list


def minOperations(n):
    """ Return sum of process until n H """
    if n < 2 or type(n) is not int:
        return 0
    values = countProcess(n)
    return sum(values)
