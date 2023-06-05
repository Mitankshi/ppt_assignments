def permute(s, left, right):
    if left == right:
        print(''.join(s))
    else:
        for i in range(left, right + 1):
            s[left], s[i] = s[i], s[left]  # Swap characters
            permute(s, left + 1, right)   # Recursively permute the remaining characters
            s[left], s[i] = s[i], s[left]  # Restore the original order (backtrack)

# Function to print all permutations of a string
def print_permutations(str):
    s = list(str)
    n = len(s)
    permute(s, 0, n - 1)

# Example usage
str = "abb"
print_permutations(str)