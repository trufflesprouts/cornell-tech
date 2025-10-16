import math


def brute_force(xs):
    n = len(xs)
    
    partition = [0] * n
    
    best_diff = math.inf
    best_partition = [0] * n # 0 = A, 1 = B

    def dfs(i, sum_a, sum_b):
        nonlocal best_diff, best_partition
        if i == n:
            diff = abs(sum_a - sum_b)
            if diff < best_diff:
                best_diff = diff
                best_partition = partition.copy()
            return
        partition[i] = 0
        dfs(i + 1, sum_a + xs[i], sum_b)
        partition[i] = 1
        dfs(i + 1, sum_a, sum_b + xs[i])

    dfs(0, 0, 0)
    return best_partition


def greedy(xs):
    n = len(xs)
    index_order = sorted(range(n), key=lambda i: xs[i], reverse=True)
    partition = [0] * n # 0 = A, 1 = B
    sum_a = 0
    sum_b = 0

    for i in index_order:
        if sum_a <= sum_b:
            partition[i] = 1
            sum_a += xs[i]
        else:
            sum_b += xs[i]

    return partition


def dp(xs):
    pass
