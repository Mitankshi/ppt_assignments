def searchRange(nums, target):
    left = 0
    right = len(nums) - 1
    start = -1
    end = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            start = mid
            end = mid

            # Search for the starting position of target
            left = left
            right = mid - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    start = mid
                    right = mid - 1
                else:
                    left = mid + 1

            # Search for the ending position of target
            left = mid + 1
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    end = mid
                    left = mid + 1
                else:
                    right = mid - 1

            break
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if start == -1:
        return [-1, -1]
    else:
        return [start, end]


nums = [1, 2, 2, 3, 4, 4, 4, 5]
target = 4
searchRange(nums=nums, target=target)
