def reverseWords(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

s = "Let's take LeetCode contest"
print(reverseWords(s))  # Output: "s'teL ekat edoCteeL tsetnoc"