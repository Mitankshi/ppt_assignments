def count_substrings(s):
    count = 0
    n = len(s)
    
    # Iterate over all possible substrings
    for i in range(n):
        for j in range(i, n):
            # Check if the substring starts and ends with the same character
            if s[i] == s[j]:
                count += 1
    
    return count

# Example usage
string = "abcab"
count = count_substrings(string)
print(count)