def product_of_array(arr):
    # Initialize the product to 1
    product = 1
    
    # Iterate through the array and multiply each element with the product
    for num in arr:
        product *= num
    
    return product

# Example usage
arr = [1, 2, 3, 4, 5]
result = product_of_array(arr)
print(result)