from functools import reduce

def square_all(numbers):
    """
    Returns a list of squares of all numbers.
    """
    return [x**2 for x in numbers]

def filter_even(numbers):
    """
    Filters and returns only the even numbers from the list.
    """
    return [x for x in numbers if x % 2 == 0]

def product_of_all(numbers):
    """
    Returns the product of all numbers in the list using reduce.
    """
    return reduce(lambda x, y: x * y, numbers)
