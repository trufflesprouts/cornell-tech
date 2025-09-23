'''
Problem 4a

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n^2).
'''
def most_frequent_difference_a(values, d_mode) -> int:
    n = len(values)
    freq = 0
    for i in range(n):
        for j in range(n):
            if i == j: continue
            ai = values[i]
            aj = values[j]
            if ai - aj == d_mode:
                freq += 1
    return freq