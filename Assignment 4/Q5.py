def arrangeCoins(n):
    left, right = 1, n
    while left <= right:
        midpoint = (left + right) // 2
        coins_required = (midpoint * (midpoint + 1)) // 2
        if coins_required > n:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return right

n = 5
print(arrangeCoins(n))