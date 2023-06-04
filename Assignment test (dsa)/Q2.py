def firstUniqChar(s):
    char_count = {}
    
    # Count the frequency of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the first non-repeating character
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    return -1

s = "leetcode"
print(firstUniqChar(s))  # Output: 0

s = "loveleetcode"
print(firstUniqChar(s))  # Output: 2

s = "aabb"
print(firstUniqChar(s))  # Output: -1