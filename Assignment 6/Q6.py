from collections import defaultdict

def findOriginalArray(changed):
    count_map = defaultdict(int)
    for num in changed:
        count_map[num] += 1

    original = []
    for num in changed:
        if count_map[num / 2] > 0:
            original.append(num / 2)
            count_map[num / 2] -= 1
        else:
            return []

    return original

changed = [1, 3, 4, 2, 6, 8]
print(findOriginalArray(changed))  # Output: [1, 3, 4]