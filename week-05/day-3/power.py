def powerN(base, n):
    if n == 1:
        return base
    else:
        return powerN(base, n - 1) * base

print(powerN(3,4))