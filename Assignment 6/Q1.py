def findPermutation(s):
    n = len(s)
    perm = []
    low = 0
    high = n
    
    for char in s:
        if char == 'I':
            perm.append(low)
            low += 1
        else:
            perm.append(high)
            high -= 1
    
    # Append the remaining number
    perm.append(low)
    
    return perm

s = "IDID"
print(findPermutation(s))  # Output: [0, 4, 1, 3, 2]