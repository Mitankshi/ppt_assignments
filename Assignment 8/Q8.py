def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False
    
    diff_s = []
    diff_goal = []
    
    for i in range(len(s)):
        if s[i] != goal[i]:
            diff_s.append(i)
            diff_goal.append(i)
    
    if len(diff_s) != 2 or len(diff_goal) != 2:
        return False
    
    if s[diff_s[0]] == goal[diff_goal[1]] and s[diff_s[1]] == goal[diff_goal[0]]:
        return True
    
    return False

s = "ab"
goal = "ba"
print(buddyStrings(s=s,goal=goal))