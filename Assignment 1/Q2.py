## Using TWO-POINTER Approach

def removeElement(nums, val):
    left = 0  # Pointer for the current element
    right = len(nums) - 1  # Pointer for the last valid element
    
    while left <= right:
        if nums[left] == val:
            # Swap the current element with the last valid element
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1  # Decrement the pointer for the last valid element
        else:
            left += 1  # Move to the next element
    
    # The value of 'left' represents the number of elements not equal to 'val'
    return left

# Example usage
nums = [3, 2, 2, 3]
val = 3
k = removeElement(nums, val)
print(k)  # Output: 2
print(nums)  # Output: [2, 2, _, _]