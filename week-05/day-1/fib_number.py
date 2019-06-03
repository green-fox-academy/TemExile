def fibnumber(x):
    a = 0
    b = 1
    for _ in range(x):
        yield a
        a, b = b, a+b

a = fibnumber(3)
print(next(a))
print(next(a))
