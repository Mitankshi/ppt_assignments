## Two-Pointer Approach

def merge(nums1, m, nums2, n):
    # Initialize pointers for nums1, nums2, and the merged array
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
    # Iterate from the end of the arrays
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] <= nums2[p2]:
            # If the element in nums1 is smaller or equal, place it in the merged array
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            # If the element in nums2 is smaller, place it in the merged array
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    
    # If there are any remaining elements in nums2, place them in the merged array
    nums1[:p2 + 1] = nums2[:p2 + 1]

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
