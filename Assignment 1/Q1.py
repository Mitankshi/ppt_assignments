##USING HASH MAP APPROACH

def twoSum(nums, target):
    num_map = {}  # Map to store complements
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[num] = i  # Store the current element and its index
    
    # If no solution is found
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # Output: [0, 1]