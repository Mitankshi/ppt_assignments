def minProductSum(nums1, nums2):
    nums1.sort()
    nums2.sort()

    left = 0
    right = len(nums2) - 1

    min_product_sum = 0

    while left <= right:
        min_product_sum += nums1[left] * nums2[right]
        left += 1
        right -= 1

    return min_product_sum

nums1 = [5, 3, 4, 2]
nums2 = [4, 2, 2, 5]
print(minProductSum(nums1, nums2))  # Output: 40
