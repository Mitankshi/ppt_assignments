def applyBackspace(s):
    result = []
    for char in s:
        if char != '#':
            result.append(char)
        elif result:
            result.pop()
    return ''.join(result)

def processString(s, t):
    processed_s = applyBackspace(s)
    processed_t = applyBackspace(t)
    return processed_s == processed_t

def backspaceCompare(s, t):
    return processString(s, t)

s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t))  # Output: True