def count_ear(n):
    if n == 0:
        return 0
    else:
        return 2 + count_ear(n - 1)

print(count_ear(3))

def count_ear_2(n):
    if n == 0:
        return 0
    elif n%2 == 0:
        return 2 + count_ear_2(n - 1)
    elif n%2 != 0:
        return 3 + count_ear_2(n - 1)
print(count_ear_2(6))

