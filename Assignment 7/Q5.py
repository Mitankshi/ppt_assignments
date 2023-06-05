def reverseStr(s, k):
    s = list(s)
    n = len(s)

    for i in range(0, n, 2 * k):
        s[i:i + k] = s[i:i + k][::-1]

    return ''.join(s)

s = "abcdefg"
k = 2
print(reverseStr(s, k))  # Output: "bacdfeg"