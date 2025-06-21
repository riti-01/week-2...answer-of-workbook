def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

n = int(input("Enter the number of rows: "))

for i in range(n):
    # Print leading spaces
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(combination(i, j), end=" ")
    print()
