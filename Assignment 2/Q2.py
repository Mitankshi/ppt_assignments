def max_candies(candyType):
    unique_types = set(candyType)
    max_types = len(unique_types)
    limit = len(candyType) // 2
    return min(max_types, limit)

candyType = [1, 1, 2, 2, 3, 3]
print(max_candies(candyType))  # Output: 3