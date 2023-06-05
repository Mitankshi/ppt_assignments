def string_length(string):
    # Base case: empty string
    if string == "":
        return 0
    # Recursive case: remove the first character and calculate length of the remaining string
    else:
        return 1 + string_length(string[1:])

# Example usage
string = "Hello, World!"
length = string_length(string)
print(length)