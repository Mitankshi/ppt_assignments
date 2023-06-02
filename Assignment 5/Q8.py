def findOriginalArray(changed):
    count = {}

    for num in changed:
        count[num] = count.get(num, 0) + 1

    original = []

    for num in changed:
        if count.get(num / 2, 0) > 0:
            original.append(int(num / 2))
            count[num / 2] -= 1
        else:
            return []

    return original

changed = [1, 3, 4, 2, 6, 8]
print(findOriginalArray(changed))

