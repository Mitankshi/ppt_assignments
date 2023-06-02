def arraysIntersection(arr1, arr2, arr3):
    p1, p2, p3 = 0, 0, 0
    result = []

    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        if arr1[p1] == arr2[p2] == arr3[p3]:
            result.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        elif arr1[p1] < arr2[p2] or arr1[p1] < arr3[p3]:
            p1 += 1
        elif arr2[p2] < arr1[p1] or arr2[p2] < arr3[p3]:
            p2 += 1
        else:
            p3 += 1

    return result

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
print(arraysIntersection(arr1, arr2, arr3))