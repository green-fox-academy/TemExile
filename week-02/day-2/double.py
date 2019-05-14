def rmdouble(file):
    a = open(file, 'r')
    b = a.readlines()
    a.close()
    c = []
    for line in b:
        d = line[::2]
        c.append(d)
    return c

print(rmdouble('duplicated-chars.txt'))