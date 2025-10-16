from functools import reduce

def factorial_rec(n):
    """
    Returns the factorial of n using recursion.
    """
    if n <= 0:
        return 1
    return n * factorial_rec(n-1)


def factorial_reduce(n):
    """
    Returns the factorial of n using functools reduce.
    """
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)
