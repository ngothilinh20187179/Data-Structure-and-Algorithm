def factorial(n):
    if (n == 1):
        return 1
    return n * factorial(n - 1)

m = factorial(4)
print("Factorial 4: ", m)