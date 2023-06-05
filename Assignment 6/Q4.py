def findMaxLength(nums):
    max_length = 0
    count = 0
    sum_count = {0: -1}

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count -= 1

        if count in sum_count:
            length = i - sum_count[count]
            max_length = max(max_length, length)
        else:
            sum_count[count] = i

    return max_length

nums = [0, 1]
print(findMaxLength(nums))  # Output: 2