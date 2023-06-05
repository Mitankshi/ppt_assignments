import math

def is_power_of_three(n):
    if n <= 0:
        return False
    # Calculate the logarithm base 3 of n
    log = math.log(n, 3)
    # Check if the logarithm is an integer
    return math.isclose(log, round(log))

# Example usage
n = 27
result = is_power_of_three(n)
print(result)