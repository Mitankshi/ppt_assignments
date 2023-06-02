def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    for p in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[p] = nums[left] ** 2
            left += 1
        else:
            result[p] = nums[right] ** 2
            right -= 1
    return result

nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))