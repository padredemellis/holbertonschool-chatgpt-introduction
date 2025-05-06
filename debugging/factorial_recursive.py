#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    ---------------------
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    -----------
    n : int
        A non-negative integer whose factorial is to be computed.

    Returns:
    --------
    int
        The factorial of 'n'. By definition, factorial(0) == 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)

