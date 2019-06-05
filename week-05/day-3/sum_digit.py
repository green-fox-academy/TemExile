def sum_digit(n):
    if n / 10 == 1:
        return 1
    elif n / 10 < 1:
        return n
    else:
        return sum_digit(n//10) + n%10

print(sum_digit(34))