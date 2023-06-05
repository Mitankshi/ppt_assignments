def factorial(N):
    result = 1
    for i in range(1, N+1):
        result *= i
    return result

N = 4
print(factorial(N=N))