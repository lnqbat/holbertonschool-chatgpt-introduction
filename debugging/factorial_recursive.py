#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Recursively calculates the factorial of a non-negative integer n.

    Parameters:
    n (int): A non-negative integer for which we want to calculate the factorial.

    Returns:
    int: The factorial of n. If n is 0, the function returns 1; otherwise, it returns n * factorial(n - 1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Check if an argument has been provided in the command line
if len(sys.argv) < 2:
    print("Usage: ./script.py <number>")
    sys.exit(1)

# Convert the argument to an integer and calculate the factorial
f = factorial(int(sys.argv[1]))

# Print the result of the factorial calculation
print(f)
