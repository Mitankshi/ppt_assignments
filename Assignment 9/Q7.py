def generate_permutations(s):
    # Convert the string to a list of characters
    chars = list(s)
    # Initialize an empty list to store the permutations
    permutations = []
    
    # Helper function to generate permutations
    def backtrack(start):
        # Base case: if start reaches the end of the string, add the current permutation to the list
        if start == len(chars):
            permutations.append("".join(chars))
            return
        
        # Recursive case: generate permutations by swapping characters
        for i in range(start, len(chars)):
            # Swap characters at indices start and i
            chars[start], chars[i] = chars[i], chars[start]
            # Recursively generate permutations for the next index
            backtrack(start + 1)
            # Restore the original order of characters (backtrack)
            chars[start], chars[i] = chars[i], chars[start]
    
    # Start the backtracking process
    backtrack(0)
    
    return permutations

# Example usage
S = "ABC"
permutations = generate_permutations(S)
print(permutations)




