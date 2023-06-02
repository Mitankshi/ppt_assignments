def maxCount(m, n, ops):
    min_a = m
    min_b = n
    for op in ops:
        min_a = min(min_a, op[0])
        min_b = min(min_b, op[1])
    return min_a * min_b

m = 3
n = 3
ops = [[2, 2], [3, 3]]
print(maxCount(m, n, ops))