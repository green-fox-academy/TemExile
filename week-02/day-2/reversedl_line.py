def reline(file):
    a = open(file, 'r')
    b = a.readlines()
    a.close()
    c = []
    for line in b:
        lines = line[::-1]
        c.append(lines)
    return c

print(reline('reversed-lines.txt'))