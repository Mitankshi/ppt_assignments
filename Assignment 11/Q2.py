def findPeakElement(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            return mid
        elif nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1

    return left

nums = [1, 2, 3, 1]
findPeakElement(nums=nums)