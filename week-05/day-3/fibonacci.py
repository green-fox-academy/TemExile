def n_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n_fibonacci(n-1) + n_fibonacci(n-2)

print(n_fibonacci(3))