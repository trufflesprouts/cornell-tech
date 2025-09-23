'''
Problem 4c

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n).
'''
from collections import Counter

def most_frequent_difference_c(values, d_mode) -> int:
    freq = Counter(values)

    if d_mode == 0:
        # count all ordered pairs of equal elements
        return sum(k * (k - 1) for k in freq.values())

    total = 0
    for ai in values:
        total += freq.get(ai - d_mode, 0)
    return total