def fibonacci(i):
    if i <= 2:
        return 1
    return fibonacci(i-2) + fibonacci(i-1)
