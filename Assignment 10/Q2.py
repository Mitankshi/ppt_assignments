def lastRemaining(n):
    if n == 1:
        return 1
    # For even n, after the first removal step, the remaining list is [2, 4, 6, ..., n].
    # The step size is 2, and the starting number is 2.
    # For odd n, after the first removal step, the remaining list is [2, 4, 6, ..., n-1].
    # The step size is 2, and the starting number is 2.
    return 2 * lastRemaining(n // 2)

# Example usage
n = 9
result = lastRemaining(n)
print(result)