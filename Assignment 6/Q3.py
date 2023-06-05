def validMountainArray(arr):
    n = len(arr)

    if n < 3:
        return False

    left = 0
    right = n - 1

    while left < right:
        if arr[left] >= arr[left + 1] or arr[right] >= arr[right - 1]:
            return False

        left += 1
        right -= 1

    return left == right

arr = [2, 1]
print(validMountainArray(arr))  # Output: False