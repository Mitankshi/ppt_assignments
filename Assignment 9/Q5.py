def find_max(arr, n):
    if n == 1:
        return arr[0]
    else:
        return max(arr[n-1], find_max(arr, n-1))

# Function to find the maximum element in the array
def maximum_element(arr):
    n = len(arr)
    return find_max(arr, n)

# Example usage
arr = [1, 4, 3, -5, -4, 8, 6]
max_element = maximum_element(arr)
print(max_element)
