# print from n to 0
def m_first_recursive(n):
    if n == 0:
        print(n)
    else:
        print(n)
        m_first_recursive(n - 1)

m_first_recursive(5)

# sum from 0 to n
def sum_number(n):
    if n == 0:
        return 0
    else:
        return n + sum_number(n - 1)

print(sum_number(5))

# print each element in a list
def rec_inc(arr):
    if len(arr) == 1:
        print(arr[0])
    else:
        print(arr[0])
        rec_inc(arr[1:])
