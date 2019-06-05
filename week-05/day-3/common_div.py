def common_div(n1, n2):
    if n2 == 0:
        return n1
    else:
        return common_div(n2, n1%n2)

print(common_div(5,23))
print(common_div(12,48))