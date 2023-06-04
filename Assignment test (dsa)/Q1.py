def moveZeroes(nums):
    left = right = 0
    n = len(nums)
    
    while right < n:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    
    while left < n:
        nums[left] = 0
        left += 1
        
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

nums = [0]
moveZeroes(nums)
print(nums)  # Output: [0]