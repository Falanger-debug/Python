def factorial(n):
    if n == 0 or n == 1:
        return 1

    for i in range(2, n):
        n *= i
    return n
