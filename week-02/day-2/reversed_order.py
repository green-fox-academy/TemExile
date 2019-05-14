def reOrder(file):
    a = open(file, 'r')
    b = a.readlines()
    a.close()
    return b[::-1]

print(reOrder('reversed-order.txt'))