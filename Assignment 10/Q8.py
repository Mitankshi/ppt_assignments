def count_consonants(s):
    consonants = 0
    vowels = "aeiouAEIOU"

    for char in s:
        if char.isalpha() and char not in vowels:
            consonants += 1

    return consonants

# Example usage
str = "Hello World"
consonant_count = count_consonants(str)
print("Number of consonants:", consonant_count)