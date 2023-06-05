def decodeString(s):
    stack = []
    
    for c in s:
        if c != ']':
            stack.append(c)
        else:
            repetition = ''
            while stack[-1] != '[':
                repetition = stack.pop() + repetition
            stack.pop()  # Remove '['
            
            count = ''
            while stack and stack[-1].isdigit():
                count = stack.pop() + count
            count = int(count)
            
            repeated_string = repetition * count
            stack.append(repeated_string)
    
    return ''.join(stack)

s = "3[a]2[bc]"
print(decodeString(s=s))