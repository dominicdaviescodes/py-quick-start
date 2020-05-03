def factorial(n):
    # return factorial of positive integer n.
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)