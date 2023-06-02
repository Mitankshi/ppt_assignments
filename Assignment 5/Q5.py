def findTheDistanceValue(arr1, arr2, d):
    distance = 0

    for num1 in arr1:
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                break
        else:
            distance += 1

    return distance

arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
print(findTheDistanceValue(arr1, arr2, d))
