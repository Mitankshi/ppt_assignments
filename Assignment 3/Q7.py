def findMissingRanges(nums, lower, upper):
    result = []
    start = lower

    for num in nums:
        if num == start:
            start += 1
        elif num > start:
            result.append([start, num - 1])
            start = num + 1

    if start <= upper:
        result.append([start, upper])

    return result

nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(findMissingRanges(nums, lower, upper))