"""
Module Name: combinatorics.py
Description: Calculation tools for counting.
Author: James Hansen
Created: 10/2/24
"""

def factorial(n):
    if ((n == 0) or (n == 1)):
        return 1
    else:
        return n * factorial(n-1)
    
def combinations(n, r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))

def permutations(n, r):
    return int(factorial(n)/factorial(n-r))
