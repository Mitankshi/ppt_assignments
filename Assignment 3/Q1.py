def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closestSum = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            currSum = nums[i] + nums[left] + nums[right]

            if abs(currSum - target) < abs(closestSum - target):
                closestSum = currSum

            if currSum < target:
                left += 1
            elif currSum > target:
                right -= 1
            else:
                return target

    return closestSum

nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))  # Output: 2