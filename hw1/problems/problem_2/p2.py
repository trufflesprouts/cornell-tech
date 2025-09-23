'''
Problem 2

input: Integer M and a list of intervals [a, b].
output: List of list of integers composing the covering.

TODO: implement a correct greedy algorithm from the homework.
'''
# implementing 2.c
# delete earliest redundant interval
def interval_covering(M: int, intervals: list) -> list:
    # sort by finish time
    intervals.sort(key=lambda interval: interval[1])
    n = len(intervals)
    overlaps = [0] * (2 * M + 1)  # covers 0, 0.5, 1, 1.5, ..., M

    # fill overlaps array
    for interval in intervals:
        l, r = get_idxs(interval)
        for i in range(l, r + 1):
            overlaps[i] += 1

    def is_redundant(interval):
        l, r = get_idxs(interval)
        for i in range(l, r + 1):
            if overlaps[i] == 1:
                return False
        return True

    removed = [False] * n
    for i, interval in enumerate(intervals):
        if is_redundant(interval):
            removed[i] = True
            l, r = get_idxs(interval)
            for i in range(l, r + 1):
                overlaps[i] -= 1

    J = [interval for i, interval in enumerate(intervals) if not removed[i]]
    return J

def get_idxs(interval):
    return interval[0] * 2, interval[1] * 2