#!/usr/bin/python3
import sys

# -------------------------------
# Function: factorial
# Description:
#   This function calculates the factorial of a given non-negative integer
#   using a recursive approach.
# Parameters:
#   - n (int): The non-negative integer for which the factorial is calculated.
# Returns:
#   - int: The factorial of the input number n. If n is 0, returns 1.
# -------------------------------
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the input number from command line arguments
f = factorial(int(sys.argv[1]))

# Print the calculated factorial
print(f)
