#!/usr/bin/python3
"""finding the minimum number of operations of copy and pasting 
a single letter to give n of that
"""
def minOperations(n):
    """
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
    """
    return n//Largest_Prime_Factor(n) + Largest_Prime_Factor(n)

def Largest_Prime_Factor(n):
    return next(n // i for i in range(1, n) if n % i == 0 and is_prime(n // i))


def is_prime(m):
    return all(m % i for i in range(2, m - 1))
