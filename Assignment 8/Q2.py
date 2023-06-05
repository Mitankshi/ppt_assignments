def checkValidString(s):
    stack = []
    star_stack = []
    
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == '*':
            star_stack.append(i)
        else:
            if stack:
                stack.pop()
            elif star_stack:
                star_stack.pop()
            else:
                return False

    while stack and star_stack:
        if stack[-1] > star_stack[-1]:
            return False
        stack.pop()
        star_stack.pop()

    return len(stack) == 0

s='()'
print(checkValidString(s=s))