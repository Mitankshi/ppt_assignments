## Carryover Operation

def plusOne(digits):
    n = len(digits)
    
    # Iterate through the digits from right to left
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            # If the current digit is less than 9, we can simply increment it and return the result
            digits[i] += 1
            return digits
        else:
            # If the current digit is 9, we set it to 0 and continue to the next digit
            digits[i] = 0
    
    # If we reach this point, it means all digits were 9
    # In this case, we need to insert a new leading digit '1'
    digits.insert(0, 1)
    return digits

# Example usage
digits = [1, 2, 3]
result = plusOne(digits)
print(result)  # Output: [1, 2, 4]