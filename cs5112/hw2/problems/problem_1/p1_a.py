# Problem 1a

# Naive
def maxsum_list_naive(xs) -> int:
    if len(xs) == 0:
        return 0
    if len(xs) == 1:
        return xs[0]
    
    return max(
        xs[0] + maxsum_list(xs[2:]),
        maxsum_list(xs[1:])
    )

# Dynamic Programming
def maxsum_list(xs) -> int:
    n = len(xs)
    if n == 0:
        return 0
    if n == 1:
        return xs[0]
    
    dp = [0] * n
    dp[0] = xs[0]
    dp[1] = max(xs[0], xs[1])
    
    for i in range(2, n):
        dp[i] = max(xs[i] + dp[i-2], dp[i-1])
    
    return dp[-1]