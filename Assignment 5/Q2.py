def arrangeCoins(n):
    k = 0
    while (k * (k + 1)) // 2 <= n:
        k += 1
    return k - 1

n = 5
print(arrangeCoins(n=n))

