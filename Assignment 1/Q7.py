## Two -Pointer approach 

def moveZeroes(nums):
    # Initialize the pointer for placing non-zero elements
    nonzero_pos = 0
    
    # Iterate through the array
    for i in range(len(nums)):
        if nums[i] != 0:
            # If the current element is non-zero, place it at the next available position
            nums[nonzero_pos] = nums[i]
            nonzero_pos += 1
    
    # Fill the remaining positions with zeros
    for i in range(nonzero_pos, len(nums)):
        nums[i] = 0

# Example usage
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]