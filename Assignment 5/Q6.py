def findDuplicates(nums):
    result = []
    for num in nums:
        index = abs(num)
        if nums[index - 1] < 0:
            result.append(index)
        else:
            nums[index - 1] *= -1
    return result

nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDuplicates(nums))