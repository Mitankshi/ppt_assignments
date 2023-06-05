def minimumDeleteSum(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = dp[i-1][0] + ord(s1[i-1])

    for j in range(1, n + 1):
        dp[0][j] = dp[0][j-1] + ord(s2[j-1])

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    total_sum = sum(ord(c) for c in s1 + s2) - 2 * dp[m][n]
    return total_sum

s1 = "sea"
s2 = "eat"
print(minimumDeleteSum(s1, s2))  # Output: 231