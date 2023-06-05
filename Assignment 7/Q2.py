def isStrobogrammatic(num):
    rotated = ""
    for c in reversed(num):
        if c == '0':
            rotated += '0'
        elif c == '1':
            rotated += '1'
        elif c == '6':
            rotated += '9'
        elif c == '8':
            rotated += '8'
        elif c == '9':
            rotated += '6'
        else:
            return False

    return rotated == num

num = "69"
print(isStrobogrammatic(num))  # Output: True