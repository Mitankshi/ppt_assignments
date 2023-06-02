def findDisappearedNumbers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    distinct_nums1 = list(set1 - set2)
    distinct_nums2 = list(set2 - set1)
    return [distinct_nums1, distinct_nums2]

nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
print(findDisappearedNumbers(nums1, nums2))