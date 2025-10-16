'''
Problem 4b

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n log n).
'''
from bisect import bisect_left, bisect_right

def most_frequent_difference_b(values, d_mode) -> int:
    values.sort()
    n = len(values)
    total = 0

    if d_mode == 0:
        i = 0
        while i < n:
            j = bisect_right(values, values[i], i, n)
            k = j - i
            total += k * (k - 1)
            i = j
        return total

    for ai in values:
        target = ai - d_mode
        lo = bisect_left(values, target)
        hi = bisect_right(values, target)
        total += (hi - lo)
    return total