from collections import Counter


def intersect(nums1, nums2):
    count1 = Counter(nums1)
    count2 = Counter(nums2)
    intersection = []

    for num in count1:
        if num in count2:
            intersection.extend([num] * min(count1[num], count2[num]))

    return intersection


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
intersect(nums1=nums1, nums2=nums2)
