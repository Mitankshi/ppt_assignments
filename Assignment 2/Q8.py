def minimumScore(nums, k):
    minimum = min(nums)
    maximum = max(nums)

    if maximum - minimum <= 2 * k:
        return 0

    mid = (minimum + maximum) // 2

    for i in range(len(nums)):
        if nums[i] <= mid:
            nums[i] = mid - k
        else:
            nums[i] = mid + k

    newMinimum = min(nums)
    newMaximum = max(nums)

    return newMaximum - newMinimum

nums = [1]
k = 0
print(minimumScore(nums, k))  # Output: 0