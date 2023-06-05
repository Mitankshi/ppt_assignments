def rotateString(s, goal):
    if len(s) != len(goal):
        return False

    concat = s + s
    return goal in concat

s = "abcde"
goal = "cdeab"
print(rotateString(s, goal))  # Output: True