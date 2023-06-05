def subsets(set):
    # Helper function to generate subsets recursively
    def generate_subsets(set, current_subset, index):
        # Base case: reached the end of the set
        if index == len(set):
            print(current_subset)
            return

        # Recursive case: choose current element and generate subsets
        generate_subsets(set, current_subset + set[index], index + 1)

        # Recursive case: do not choose current element and generate subsets
        generate_subsets(set, current_subset, index + 1)

    # Call the helper function with initial values
    generate_subsets(set, "", 0)

# Example usage
set = "abc"
subsets(set)